#takes a mean of numbers input to command line

import sys

# sys.argv is an array of inputs to the command line
# here sys.argv[0] input is mean.py

#checks to make sure there are inputs
if len(sys.argv) == 1:
    print 'Error: No arguments given.'
    exit()

#takes the mean of all inputs
sum = 0
for num in sys.argv[1:]:
    sum += float(num)

#prints the mean
print sum / (len(sys.argv) - 1)
