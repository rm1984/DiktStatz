#!/usr/bin/env python3

#
# DiktStatz.py
# ------------
# A simple Python script that prints some useful statistical information by
# reading a given passwords dictionary.
#
# Coded by: Riccardo Mollo (riccardomollo84@gmail.com)
#

#### TODO:
#### - ???

import argparse
import csv
import os
import re
import signal
import sys
from prettytable import PrettyTable
from termcolor import colored

# constants
SPECIAL_CHARS = '[@_!#$%^&*()<>?/\\|}{~:]=/'

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

def error(message):
    print(colored('ERROR!', 'red', attrs = ['reverse', 'bold']) + ' ' + message)

def percent(n1, n2):
    return '{0:.2f}%'.format((n1 / n2 * 100))

def count_chars(file):
    f = open(file, 'r')
    d = f.read().replace('\n', '')
    n = len(d)
    f.close()

    return n

def main(argv):
    parser = argparse.ArgumentParser(prog = 'diktstatz.py')
    parser.add_argument('-d', '--dictionary', help = 'text file containing a lot of juicy passwords', required = True)
    parser.add_argument('-m', '--max-length', help = 'only passwords with length up to this value will be considered', required = False)
    parser.add_argument('-o', '--output', help = 'save results\' output as a CSV file', required = False)
    args = parser.parse_args()
    dict_file = args.dictionary

    if not os.path.isfile(dict_file):
        error('File "' + dict_file + '" does not exist or is not readable.')
        sys.exit(1)

    dict_size = count_chars(dict_file)

    try:
        max_length = len(max(open(dict_file), key = len))
    except ValueError as valueerror:
        error('File "' + dict_file + '" seems to be empty.')
        sys.exit(1)

    output = args.output

    if args.max_length is not None:
        if int(args.max_length) > 0 and int(args.max_length) <= max_length:
            max_length = int(args.max_length) + 1

    logo()

    total = sum(1 for i in open(dict_file, 'r'))
    semit = 0
    counters = {}

    for i in range(max_length):
        counters[i] = 0

    sc_re = re.compile(SPECIAL_CHARS)
    wn_re = re.compile('[a-zA-Z]+\d+$', re.IGNORECASE) # eg: "Foo123" or "password999" or "Test0"
    alnum = 0
    alpha = 0
    digit = 0
    lower = 0
    upper = 0
    specl = 0
    wdnum = 0

    with open(dict_file) as dict:
        for password in dict:
            password = password.rstrip('\n')
            l = len(password)

            if l <= max_length:
                if password.isalnum():
                    alnum += 1

                if password.isalpha():
                    alpha += 1

                if password.isdigit():
                    digit += 1

                if password.islower():
                    lower += 1

                if password.isupper():
                    upper += 1

                if sc_re.search(password) is not None:
                    specl += 1

                if wn_re.search(password) is not None:
                    wdnum += 1

                try:
                    counters[l] += 1
                    semit += 1
                except IndexError as indexerror:
                    pass
                except Exception as exception:
                    pass

    print('Dictionary file:       ' + os.path.abspath(dict_file))
    print('Dictionary size:       ' + str(dict_size) + ' bytes')
    print('Max password length:   ' + str(max_length - 1) + ' characters' + (' (forced by user)' if args.max_length is not None and total != semit else ''))
    print('Avg password length:   ' + str(round(dict_size / total)) + ' characters')
    print('Total passwords:       ' + str(total))
    print('Considered passwords:  ' + str(semit) + ' (' + percent(semit, total) + ')')
    print()

    if semit == 0:
        print('No passwords with length less or equal to ' + str(max_length) + ' characters.')
    else:
        pwtable = PrettyTable()
        chtable = PrettyTable()

        if output is not None:
            try:
                csv_file = open(output, 'w')
                writer = csv.writer(csv_file)
            except PermissionError as permissionerror:
                error('Cannot write file "' + output + '". Permission denied.')
                sys.exit(1)
            except IsADirectoryError as isadirectoryerror:
                error('"' + output + '" is a directory, not a file.')
                sys.exit(1)

        if args.max_length is None:
            pwtable.field_names = ['Length', 'Passwords', 'Total %']
        else:
            pwtable.field_names = ['Length', 'Passwords', 'Relative %', 'Total %']

        if output is not None:
            writer.writerow(pwtable.field_names)

        pwtable.align['Length'] = 'r'
        pwtable.align['Passwords'] = 'r'

        if args.max_length is None:
            pwtable.align['Total %'] = 'r'
        else:
            pwtable.align['Relative %'] = 'r'
            pwtable.align['Total %'] = 'r'

        pwtable.sortby = 'Passwords'
        pwtable.reversesort = True

        for i in range(max_length):
            if counters[i] > 0:
                try:
                    if args.max_length is None:
                        row = [i, counters[i], percent(counters[i], total)]
                    else:
                        row = [i, counters[i], percent(counters[i], semit), percent(counters[i], total)]

                    pwtable.add_row(row)

                    if output is not None:
                        writer.writerow(row)
                except KeyError as keyerror:
                    print(keyerror)

        print(pwtable)
        print()

        chtable.field_names = ['Password type', 'Count', 'Count %']
        chtable.align['Password type'] = 'l'
        chtable.align['Count'] = 'r'
        chtable.align['Count %'] = 'r'

        chtable.add_row(['Alphanumeric', alnum, percent(alnum, semit)])
        chtable.add_row(['Alphabetic only', alpha, percent(alpha, semit)])
        chtable.add_row(['Digits only', digit, percent(digit, semit)])
        chtable.add_row(['Lowercase only', lower, percent(lower, semit)])
        chtable.add_row(['Uppercase only', upper, percent(upper, semit)])
        chtable.add_row(['With special chars', specl, percent(specl, semit)])
        chtable.add_row(['"WordNumber" format', wdnum, percent(wdnum, semit)])

        print(chtable)

        if output is not None:
            csv_file.close()
            print()
            print('Output saved to CSV file: ' +  output)
    print()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])
