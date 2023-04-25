# FILE INPUT
# print('Enter a file name:')
inp = input('')
d = dict()

try:
    fhandle = open(inp)
except:
    print('File cannot be opened.')
    quit()

# FOR LOOP READING FILE AND APPENDING DICTIONARY
for line in fhandle:
    if not line.startswith('From '):
        continue
    else:
        # print(line)
        words = line.split()
        words = words[1]
        d[words] = d.get(words, 0) + 1

# print(d)
largest = None

# FOR MAX LOOP
for word,count in d.items():
    if largest is None or count > largest:
        # print('executing',word)
        largest = count
        key = word
    else:
        continue

print(key, largest)
