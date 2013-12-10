#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import time
import tempfile

# See: w3af.core.controllers.ci.moth
FMT = '/tmp/moth-%s.txt'
HTTP_ADDRESS_FILE = FMT % 'http'
HTTPS_ADDRESS_FILE = FMT % 'https'

DELTA = 0.5

TRACEBACK = 'Traceback (most recent call last):'
ARTIFACTS_DIR = os.environ.get('CIRCLE_ARTIFACTS', tempfile.gettempdir())
DAEMON_START_LOG = os.path.join(ARTIFACTS_DIR, 'setup-moth-nohup.log')

if os.path.exists(DAEMON_START_LOG):
    daemon_log = file(DAEMON_START_LOG).read()

    if TRACEBACK in daemon_log:
        print('Traceback found in daemon start log. Moth failed to start.')
        print(daemon_log)
        sys.exit(-1)

wait_time = 0
print('Waiting for moth to start', end='')

while True:
    time.sleep(DELTA)
    wait_time += DELTA
    
    if os.path.exists(HTTP_ADDRESS_FILE) and os.path.exists(HTTPS_ADDRESS_FILE):
        time.sleep(DELTA * 2)
        print('')
        print('Started moth in %s seconds.' % wait_time)
        break  
    else:
        print('.', end='')
        sys.stdout.flush()
