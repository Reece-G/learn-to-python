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
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count = count + 1
print('There were',count,'lines in the file',name,'that starts with "from"')
