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
        words = words[5]
        time = words[0:2]
        d[time] = d.get(time, 0) + 1

for key, val in d.items():
    l.append((key, val))
l.sort()

for key, val in l:
    print(key, val)
