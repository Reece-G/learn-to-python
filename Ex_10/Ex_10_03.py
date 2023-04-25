import string
print('Enter file name:')
inp = input('')
d = dict()
l = list()

try:
    fhand = open(inp)
except:
    print('File name not valid.')

# For loops to count lowercase letters only, removing everything else.
for line in fhand:
    line = line.lower().strip()
    words = line.split()
    for word in words:
        for letter in word:
            if letter in string.ascii_lowercase:
                d[letter] = d.get(letter, 0) + 1
            else:
                continue

# Sorting the count of letters using a list
for key, val in d.items():
    l.append((val, key))
l.sort(reverse = True)

# Final print statement for sequential printing of letters and their count. Highest to lowest
for val, key in l:
    print(key, val)
