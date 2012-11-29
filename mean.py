# This is on the handle_file branch.
import sys

# Must have at least one value.
if len(sys.argv) == 1:
    print 'Error: No arguments given.'
    exit()

# Calculate sum of command-line arguments.
n = 0
sum = 0
for num in open(sys.argv[1]):
    sum += float(num)
    n += 1

print sum / n

