name = input('Enter a file name: ')
count = 0
try:
    fhand = open(name)
except:
    print('Enter a valid text file.')
    quit()
for line in fhand:
    line = line.upper().rstrip()
    print(line)

    # This is a added conditional to stop after 5 iterations to save time.
    count = count + 1
    if count == 5:
        print('done')
        quit()
