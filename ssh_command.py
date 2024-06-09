#!/usr/bin/env python3

import shlex
import os
from sirtunnel import run

if __name__ == "__main__":

    try:
        arg_string = os.environ["SSH_ORIGINAL_COMMAND"]
    except KeyError:
        print("This script is intended to be run as a SSH forced command (eg. via authorized_keys command= directive)")
        exit(1)

    args = shlex.split(arg_string)
    run(args)
