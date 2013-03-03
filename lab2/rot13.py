import string
import fileinput

table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

for line in fileinput.input():
        line = line.rstrip()
        print string.translate(line, table)
