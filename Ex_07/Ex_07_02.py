# User inputs and initialising variables
name = input('Enter a file name: ')
total = None
count = 0

# Error check the input and run the code.
try:
    fhand = open(name)
except:
    print('Invalid input.')
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    search = line.find(':')
    line = float(line.lstrip()[search + 1:])
    count = count + 1
    if total is None:
        total = line
        continue
    total = total + line

print('Average spam confidence:',total/count)
