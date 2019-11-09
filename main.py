#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
[Description]
"""

__author__ = 'MapleCCC, <littlelittlemaple@gmail.com>'

import argparse
import sys

from utils import *


def initialize_argparse(parser: argparse.ArgumentParser)->None:
    parser.add_argument(
        '-d',
        '--debug',
        dest='enabled_debug_mode',
        action='store_true',
        default=False,
        help='Enabled debug mode')


def main():
    import argparse
    parser = argparse.ArgumentParser(description='')
    initialize_argparse(parser)
    args = parser.parse_args()

    if not args.enabled_debug_mode:
        # this clean trick also has desirable side effect that exception
        # chaining is suppressed.
        sys.excepthook = lambda exctype, exc, traceback: print(
            f"{exctype.__name__}: {exc}")


if __name__ == '__main__':
    main()
