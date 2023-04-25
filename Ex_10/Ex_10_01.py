print('Enter a file name:')
inp = input('')
d = dict()
l = list()

try:
    fhandle = open(inp)
except:
    print('File cannot be opened.')
    quit()


for line in fhandle:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        words = words[1]
        d[words] = d.get(words, 0) + 1

# Listing the items of the dictionary to sort later
for key, val in d.items():
    l.append((val, key))

# Sorting list and outputting most common email
l.sort()
l.reverse()
x, y = l[0]
print(y, x)
