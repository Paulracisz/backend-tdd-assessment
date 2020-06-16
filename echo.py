#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Paul Racisz"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    result = ns.text
    if not args:
        parser.print_usage()
        sys.exit()
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()
    if ns.title:
        result = result.title()
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
