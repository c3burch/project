#takes a mean of numbers inputed to command line

import sys

#sys.argv is an array of inputs to the command line

sum = 0
for num in sys.argv[1:]:
    sum += float(num)

print sum / (len(sys.argv) - 1)
