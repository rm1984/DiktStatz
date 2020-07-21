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
$ ./diktstatz.py -d /tmp/dict.txt -m 16 -o /tmp/dict.csv 
 _          __            
| \ o | _|_(_ _|_ _ _|_ _ 
|_/ | |< |___) |_(_| |_ /_

DiktStatz - Statistics for password dictionaries
Coded by: Riccardo Mollo

Dictionary file:       /tmp/dict.txt
Dictionary size:       84458277 bytes
Max password length:   16 characters (forced by user)
Avg password length:   8 characters
Total passwords:       10000000
Considered passwords:  9972772 (99.73%)

+--------+-----------+------------+---------+
| Length | Passwords | Relative % | Total % |
+--------+-----------+------------+---------+
|      8 |   2734760 |     27.42% |  27.35% |
|      9 |   1598275 |     16.03% |  15.98% |
|      6 |   1486136 |     14.90% |  14.86% |
|     10 |   1336621 |     13.40% |  13.37% |
|      7 |   1246595 |     12.50% |  12.47% |
|     11 |    566453 |      5.68% |   5.66% |
|     12 |    345499 |      3.46% |   3.45% |
|      5 |    212806 |      2.13% |   2.13% |
|     13 |    150455 |      1.51% |   1.50% |
|     14 |    102168 |      1.02% |   1.02% |
|      4 |     56090 |      0.56% |   0.56% |
|     15 |     52020 |      0.52% |   0.52% |
|     16 |     44838 |      0.45% |   0.45% |
|      3 |     35961 |      0.36% |   0.36% |
|      2 |      3991 |      0.04% |   0.04% |
|      1 |       104 |      0.00% |   0.00% |
+--------+-----------+------------+---------+

+--------------------+---------+---------+
| Password type      |   Count | Count % |
+--------------------+---------+---------+
| Alphanumeric       | 9824938 |  98.52% |
| Alphabetic only    | 2282558 |  22.89% |
| Digits only        | 1176271 |  11.79% |
| Lowercase only     | 7641431 |  76.62% |
| Uppercase only     |  207716 |   2.08% |
| With special chars |   79333 |   0.80% |
+--------------------+---------+---------+

Output saved to CSV file: /tmp/dict.csv
```