#!/usr/bin/python

from __future__ import print_function
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <your-output-file>".format(sys.argv[0]))
        return -1
    lineno = 1
    key_words = set(("init", "error"))
    with open(sys.argv[1]) as of:
        for line in of:
            line = line.rstrip()
            if len(line) < 4:
                print("Error Line {}: number of chars is less than 4".format(lineno))
                continue
            if line[0:4] != "init":
                print("Error Line {}: Every line should start with \"init\": \"{}\" is found.".format(lineno, line[0:4]))
            words = set(line.split(" "))
            words = words - key_words
            for word in words:
                if len(word) != 1:
                    print("Error Line {}: Invalid output \"{}\" (process names have only single char)".format(lineno, word))
            lineno += 1

if __name__ == "__main__":
    print("""
********************************************************************************
Expectations:
1. The output file should contain a separate line for each test sequence
2. Each line should start with "init"; this should be followed by a series of
single characters separated by blanks.
3. Valid output: "init", "error", <single-char-process-names>
********************************************************************************
""")
    main()
    print("done.")
    print()
