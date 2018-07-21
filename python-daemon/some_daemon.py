#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from daemon import DaemonContext
from daemon.pidfile import PIDLockFile
import logging
import logging.config
import time
import signal
import argparse

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("app")


def reload_program_config():
    """docstring for reload_program_config"""
    logger.warn('stop daemon')
    exit()


logger.info('start daemon')

parser = argparse.ArgumentParser(version='1.0')
parser.add_argument('-d', action="store_true", default=False,
                    help='daemonize')
args = parser.parse_args()
if args.d:
    dc = DaemonContext(
        pidfile = PIDLockFile('/tmp/lost.pid'),
        files_preserve = [logger.handlers[0].stream],
        signal_map = {
            signal.SIGTERM: reload_program_config
        }
    )
    with dc:
        while True:
            logger.info('daemon working')
            time.sleep(2)
else:
    while True:
        logger.info('daemon working')
        time.sleep(2)
