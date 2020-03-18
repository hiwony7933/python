#readlines03.py
import sys

fname = sys.argv[1]
f = open(fname, 'r')

lines = f.readlines()
for line in lines:
     print(line)

f.close()
