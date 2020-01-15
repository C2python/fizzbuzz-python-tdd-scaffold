#!/usr/bin/python3.7

# -*- coding:utf-8 -*-

# Author: zhangwen1
# Email: zhangwen1@unionpay.com

# Desc: Print FizzBuzz.

import sys
import argparse
import logging


def fizzbuzz(id):
    if id % 15 == 0:
        return "FizzBuzz"
    elif id % 5 == 0:
        return "Fizz"
    elif id % 3 == 0:
        return "Buzz"
    return None


def print_fizzbuzz(seq):
    for id in range(1, seq+1):
        output = fizzbuzz(id)
        if output is not None:
            print(output)
    return 0


def format_commands(progname, commands_list):
    help = "Commands:\n"
    for cmd in commands_list:
        help += "  %s\n      %s %s\n" % (cmd["label"], progname, cmd["param"])
    return help


def get_commmand_list():
    return [
        {"cmd": "print fizzbuzz", "label": "Print FizzBuzz",
         "param": "--seq seq", "func": print_fizzbuzz, "argc": 1}
    ]


def main():
    commands_list = get_commmand_list()

    epilog = format_commands(sys.argv[0].split('/')[-1], commands_list)
    parser = argparse.ArgumentParser(description='FizzBuzz Project.',
                                     epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--seq', type=int,
                        default=None, help="Print Fizzbuzz Until Seq")
    args = parser.parse_args()
    print_fizzbuzz(args.seq)


if __name__ == '__main__':
    sys.exit(main())
