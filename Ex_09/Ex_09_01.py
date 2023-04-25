print('Enter a file name:')
inp = input('')
fhandle = open(inp)
d = {}

for line in fhandle:
    for words in line.split():
        if words not in d:
            d[words] = 1
            # print('new')
        else:
            d[words] = d[words] + 1
            # print('+1')
print(d)

ask = input('Enter a word: ')
if ask in d:
    inp = inp + '!'
    print('Yes',ask,'is in',inp)
else:
    print('Sorry',ask,'is not in',inp)
