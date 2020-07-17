#!/usr/bin/env python3

import argparse
import signal
import sys
from prettytable import PrettyTable
from termcolor import colored

# constants
MAX_LENGTH = 16

def signal_handler(s, frame):
    if s == 2: # SIGINT
        print('You pressed Ctrl+C!')
        print('Goodbye!')
        sys.exit()

def logo():
    print(colored(' _          __            ', 'cyan'))
    print(colored('| \\ o | _|_(_ _|_ _ _|_ _ ', 'cyan'))
    print(colored('|_/ | |< |___) |_(_| |_ /_', 'cyan'))
    print()
    print(colored('DiktStatz - Statistics for password dictionaries', 'cyan'))
    print(colored('Coded by: Riccardo Mollo', 'cyan'))
    print()

def percent(n1, n2):
    return '{0:.2f}%'.format((n1 / n2 * 100))

def main(argv):
    parser = argparse.ArgumentParser(prog = 'diktstatz.py')
    parser.add_argument('-d', '--dictionary', help = 'text file containing a lot of juicy passwords', required = True)
    parser.add_argument('-m', '--max-length', help = 'only passwords with length up to this value will be considered (default: 16)', required = False)
    args = parser.parse_args()
    dict_file = args.dictionary
    max_length = MAX_LENGTH if args.max_length is None else int(args.max_length)

    logo()

    total = sum(1 for i in open(dict_file, 'r'))
    semit = 0

    print('Dictionary: ' + dict_file)
    print("Max password length considered: " + str(max_length))
    print("Total number of passwords: " + str(total))

    counters = {}

    for i in range(max_length):
        counters[i] = 0

    with open(dict_file) as dict:
        for password in dict:
            l = len(password.rstrip('\n'))

            try:
                counters[l] += 1
                semit += 1
            except IndexError as indexerror:
                pass
            except Exception as exception:
                pass

    print("Partial number of passwords: " + str(semit))
    print()

    table = PrettyTable()
    table.field_names = ['Length', 'Passwords', 'Relative Percentage', 'Total Percentage']
    table.align['Length'] = 'r'
    table.align['Passwords'] = 'r'
    table.align['Relative Percentage'] = 'r'
    table.align['Total Percentage'] = 'r'
    table.sortby = 'Passwords'
    table.reversesort = True

    for i in range(max_length):
        try:
            table.add_row([i, counters[i], percent(counters[i], semit), percent(counters[i], total)])
        except KeyError as keyerror:
            print(keyerror)

    print(table)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])