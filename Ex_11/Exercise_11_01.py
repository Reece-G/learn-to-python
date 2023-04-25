import re
inp = input('Enter a regular expression: ')
fhand = open('mbox.txt')
print(inp)
count = 0
for line in fhand:
    line = line.strip()
    x = re.findall(inp, line)
    if len(x) > 0:
        count = count + 1
    continue
print('mbox.txt had',count,'lines that matched',inp)
