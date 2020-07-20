# DiktStatz

**DiktStatz** is a simple Python script that prints some useful statistical information by reading a given passwords dictionary.

**Usage:**
```
usage: diktstatz.py [-h] -d DICTIONARY [-m MAX_LENGTH] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -d DICTIONARY, --dictionary DICTIONARY
                        text file containing a lot of juicy passwords
  -m MAX_LENGTH, --max-length MAX_LENGTH
                        only passwords with length up to this value will be considered
  -o OUTPUT, --output OUTPUT
                        save results' output as a CSV file
```

**Example output:**
```
$ ./diktstatz.py -d /tmp/dict.txt -o /tmp/dict.csv
 _          __            
| \ o | _|_(_ _|_ _ _|_ _ 
|_/ | |< |___) |_(_| |_ /_

DiktStatz - Statistics for password dictionaries
Coded by: Riccardo Mollo

Dictionary file:       /tmp/dict.txt
Dictionary size:       84458277 bytes
Max password length:   30 characters
Avg password length:   8 characters
Total passwords:       10000000
Considered passwords:  10000000 (100.00%)

+--------+-----------+------------+
| Length | Passwords | Percentage |
+--------+-----------+------------+
|      8 |   2734760 |     27.35% |
|      9 |   1598275 |     15.98% |
|      6 |   1486136 |     14.86% |
|     10 |   1336621 |     13.37% |
|      7 |   1246595 |     12.47% |
|     11 |    566453 |      5.66% |
|     12 |    345499 |      3.45% |
|      5 |    212806 |      2.13% |
|     13 |    150455 |      1.50% |
|     14 |    102168 |      1.02% |
|      4 |     56090 |      0.56% |
|     15 |     52020 |      0.52% |
|     16 |     44838 |      0.45% |
|      3 |     35961 |      0.36% |
|     17 |      8706 |      0.09% |
|     18 |      6524 |      0.07% |
|      2 |      3991 |      0.04% |
|     19 |      3468 |      0.03% |
|     20 |      3368 |      0.03% |
|     21 |      1201 |      0.01% |
|     22 |      1057 |      0.01% |
|     23 |       639 |      0.01% |
|     24 |       592 |      0.01% |
|     25 |       561 |      0.01% |
|     30 |       334 |      0.00% |
|     26 |       295 |      0.00% |
|     27 |       193 |      0.00% |
|     28 |       176 |      0.00% |
|     29 |       114 |      0.00% |
|      1 |       104 |      0.00% |
+--------+-----------+------------+

+-----------------+---------+
| Password type   |   Count |
+-----------------+---------+
| Alphanumeric    | 9840534 |
| Alphabetic only | 2285382 |
| Digits only     | 1176834 |
| Lowercase only  | 7656334 |
| Uppercase only  |  208356 |
+-----------------+---------+

Output saved to CSV file: /tmp/dict.csv
```