import sys

script, filename = sys.argv

file = open(filename)
file_cntnt = file.read()

print(file_cntnt)

