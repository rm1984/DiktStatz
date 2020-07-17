#!/usr/bin/env python3

import signal
import sys
import texttable
from termcolor import colored

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
    dict_file = 'dict2.txt'

    logo()

    MAX_PASSWORD_LENGTH = 16

    total = sum(1 for i in open(dict_file, 'r'))
    semit = 0

    print('Dictionary: ' + dict_file)
    print("Max password length considered: " + str(MAX_PASSWORD_LENGTH))
    print("Total number of passwords: " + str(total))

    counters = {}

    for i in range(MAX_PASSWORD_LENGTH):
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

    table = texttable.Texttable()
    thead = ['Length', 'Passwords', 'Percentage']
    table.header(thead)

    length = []
    passwords = []
    percentage = []

    for i in range(MAX_PASSWORD_LENGTH):
        try:
            length.append(i)
            passwords.append(counters[i])
            percentage.append(percent(counters[i], semit))
        except KeyError as keyerror:
            print(keyerror)

    for row in zip(length, passwords, percentage):
        table.add_row(row)

    table.sortby = 'Passwords'
    print(table.draw())

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main(sys.argv[1:])