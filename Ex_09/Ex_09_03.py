print('Enter a file name:')
inp = input('')
d = dict()

try:
    fhandle = open(inp)
except:
    print('File cannot be opened.')
    quit()

for line in fhandle:
    if not line.startswith('From '):
        continue
    else:
        # print(line)
        words = line.split()
        words = words[1]
        d[words] = d.get(words, 0) + 1
print(d)
