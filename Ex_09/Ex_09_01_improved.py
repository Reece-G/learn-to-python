print('Enter a file name:')
inp = input('')
fhandle = open(inp)
d = {}

# Improved counting loop using the get function of dictionaries, rather than
# the if statement in Ex_09_01.py (four lines of code become one.)
for line in fhandle:
    for words in line.split():
        d[words] = d.get(words, 0) + 1

print(d)


ask = input('Enter a word: ')
if ask in d:
    inp = inp + '!'
    print('Yes',ask,'is in',inp)
else:
    print('Sorry',ask,'is not in',inp)
