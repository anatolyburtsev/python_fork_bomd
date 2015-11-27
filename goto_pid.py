#!/usr/bin/python

import os
import sys

target = int(sys.agrv[1])


n = 0

while True:
    n = n+1
    pid = os.fork()
    if pid != 0:
        sys.exit(0)
