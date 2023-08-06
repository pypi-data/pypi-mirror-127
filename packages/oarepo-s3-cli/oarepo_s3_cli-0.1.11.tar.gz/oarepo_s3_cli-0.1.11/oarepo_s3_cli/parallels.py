# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CESNET.
#
# OARepo-S3-CLI is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

""" OARepo S3 client parallel processing lib."""

import sys, time, signal, logging
import multiprocessing as mp
from datetime import timedelta
from oarepo_s3_cli.utils import *

logger = logging

class Parallels():
    def __init__(self, worker, idle_callback, num_parts, parts_unfin, parallel=0, quiet=False):
        self.worker = worker
        self.idle_callback = idle_callback
        self.num_parts = num_parts
        self.parts_unfin = parts_unfin
        self.pool_size = MAX_PARALLEL if parallel == 0 else parallel
        if self.pool_size > len(self.parts_unfin): self.pool_size = len(self.parts_unfin)
        self.mon_timeout = MON_TIMEOUT
        self.killed = False
        self.pn = None
        self.quiet = quiet
        self.stats = Stats(self.num_parts, self.num_parts-len(self.parts_unfin))
        self.spinner = Spinner()
        self.start = 0

    def signal_handler(self, signumber, stack_frame):
        signame = get_signame(signumber)
        logger.debug(
            f"\n{procname()} pn:{self.pn}: \
            Caught signal \"{signame}\" ({signumber})")
        # if mp.current_process().name == 'MainProcess' and not self.killed:
        if mp.current_process().name == 'MainProcess':
            secho(f"\nKeyboard interrupt, waiting for child processes ... ", quiet=self.quiet)
            if not self.killed: self.killed = True
            else:
                logger.debug(f"\n{procname()}: exit")
                sys.exit(STATUS_KILLED)
        else:
            raise SignalException(self.pn, (f'Signal "{signame}"({signumber})', signumber))
            # raise SignalException(self.pn, f'Signal "{signame}"({signumber})')

    def output(self, signumber=0, stack_frame=None):
        elapsed = round(time.time() - self.start)
        timer = round(time.time() - self.stats.ts)
        barchar = '#'
        spinchar = self.spinner.get()
        elapsed_f = str(timedelta(seconds=elapsed))
        fin_perc = self.stats.finished * 100 / self.num_parts
        fin_bar = round(self.stats.finished * BAR_LENGTH / self.num_parts)
        bar = f"{barchar * fin_bar}{spinchar if fin_bar < BAR_LENGTH else ''}{' ' * (BAR_LENGTH - fin_bar - 1)}"
        w = len(str(self.num_parts))
        term4 = f"terminating:{self.stats.for_terminate}" if self.stats.for_terminate>0 else ''
        timer_f = "%6s" % (f"({timer}s)",) if timer>0 else ''
        vals = (elapsed_f, fin_perc, bar, self.stats.pending, self.stats.running,
                self.stats.finished, self.stats.failed, term4, timer_f)
        msg = f"%s %3d%% [%s] pending:%-{w}d; started:%-{w}d; finished:%-{w}d; failed:%-{w}d %s %s" % vals
        secho(f"\r %-100s." % (msg,), nl=False, quiet=self.quiet)
        sys.stdout.flush()
        if self.stats.remaining>0: signal.alarm(CYCLE_SLEEP)


    def worker_wrapper(self, pn, val):
        self.pn = pn
        signal.signal(signal.SIGINT, self.signal_handler)
        # signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGALRM, self.signal_handler)
        alrms = signal.alarm(WORKER_TIMEOUT)
        logger.debug(f"\n>#{pn} {procname()} (alarms:{alrms}, val:{val})")
        try:
            res = self.worker(pn, val)
        except Exception as e:
            logger.debug(f"\n..#{pn} caught and raising Exception \"{e}\" {procname()}")
            # raise e
            # https://stackoverflow.com/questions/6062576/adding-information-to-an-exception/6062799
            raise type(e)((pn,)+e.args).with_traceback(sys.exc_info()[2])
        finally:
            alrms = signal.alarm(0)
        logger.debug(f"\n<#{pn} {procname()} (alrms:{alrms})")
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        return pn, res

    def main(self):
        futs = [None for i in range(self.num_parts)]
        results = [None for i in range(self.num_parts)]
        # --- handlers: ---
        def ok_cb(res):
            logger.debug(f'\nCB:{procname()} {res}')
            results[res[0]-1] = res[1]
            self.stats.finish()

        def err_cb(res):
            logger.debug(f'\nERR CB:{procname()} {res}/{type(res)}')
            # pn, msg = res.args
            if len(res.args) > 1:
                pn, msg = res.args
                results[pn - 1] = res
            self.stats.fail()

        # --- process pool init: ---
        logger.debug(f'Start main: {120*"="}')
        self.start = time.time()
        pool = None
        try:
            pool = mp.Pool(self.pool_size)
            logger.debug(f'main: Start {self.pool_size} parallel uploads of {self.num_parts} parts')
            for partNum in self.parts_unfin:
                futs[partNum-1] = pool.apply_async(
                    self.worker_wrapper, args=(partNum, f"val-{partNum}",),
                    callback=ok_cb, error_callback=err_cb)
                # self.stats.start()
            self.stats.start(self.pool_size)
        except Exception as e:
            logger.debug(f"\n{procname()}: Pool Exception: {e}")
        if pool is not None:
            logger.debug(f"\n{procname()}: closing pool:")
            pool.close()
            logger.debug(f"{procname()} pool closed.")
        else:
            logger.debug(f"{procname()} no pool started.")
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGALRM, self.output)
        alrms = signal.alarm(CYCLE_SLEEP)

        # --- main cycle: ---
        try:
            while True:
                self.secs = round(time.time() - self.start)
                self.timer = round(time.time() - self.stats.ts)

                #self.output()
                if self.killed:
                    pool.terminate()
                    break
                if self.stats.remaining == 0: break
                if self.timer > self.mon_timeout:
                    logger.critical(f"\nMonitor timeout ({MON_TIMEOUT}s) reached")
                    secho(f"\nMonitor timeout ({MON_TIMEOUT}s) reached", prefix='\nERR', fg='red')
                    break
                self.idle_callback()
                time.sleep(PRESIGN_REQ_SLEEP)
        except Exception as e:
            raise Exception(None, f'Main cycle Exception {e})')
        alrms = signal.alarm(0)
        reason = 'finished' if self.stats.remaining == 0 else 'interrupt' if self.killed else 'timeout?'
        logger.debug(f"\n{'-' * 10} main cycle ended ({reason}) {'-' * 10}")

        # --- scan results from futures: ---
        for i in range(len(futs)):
            partNum, fut, res = i + 1, futs[i], results[i]
            logger.debug(f' scan #{partNum} res:{res}; fut {fut}')
            if res is not None: continue
            if fut is None: continue
            logger.debug(f'final waiting for fut {partNum}: ')
            try:
                j, res = fut.get(FORCED_GET_TIMEOUT)
                self.stats.finish()
                assert partNum == j
                results[partNum-1] = res
                logger.debug(f"OK: #{partNum} get: {res}({type(res) if isinstance(res, Exception) else ''})")
            except mp.context.TimeoutError as e:
                logger.debug(f'\nERR: #{partNum} upload failed (e.args:{e.args})')
                self.stats.terminate()
            except Exception as e:
                logger.debug(f'\nERR: #{partNum} result is Exception {e} (e.args:{e.args})')
                results[i] = e
                # self.stats.fail()
        self.output()

        logger.debug(f"\n{'-' * 3} scan cycle ended {'-' * 3}")
        try:
            if self.stats.remaining > 0 or self.stats.for_terminate > 0:
                logger.debug(f"\nmain: terminating pool ...")
                pool.terminate()
            logger.debug(f"\nmain: joining pool ...")
            pool.join()
        except Exception as e:
            logger.error(f"\n{procname()} Join exception: {e}({type(e)})")
        logger.debug(f'\n{procname()} joined')

        # --- check Exceptions in results: ---
        logger.debug("\nresults: ")
        for i in range(len(results)):
            item = results[i]
            if isinstance(item, Exception):
                item = f'Ex{item}({type(item)})'
            logger.debug(f'  {i+1}:{item} ')
        st = STATUS_OK if self.stats.remaining == 0 and self.stats.failed == 0 else STATUS_UPLOAD_UNCOMPLETED
        prefix = '\nOK' if st == STATUS_OK else '\nERR'
        fg = 'green' if st == STATUS_OK else 'red'
        secho(f"remaining:{self.stats.remaining}, failed:{self.stats.failed}", prefix=prefix, fg=fg, quiet=self.quiet)
        logger.debug(f'\nmain: Done [{st}].')
        return (st, results)

