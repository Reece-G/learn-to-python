fhand = open('romeo.txt')
list = []

for line in fhand:
    words = line.split()
    for x in words:
        x = x.lower()
        if not x in list:
            list.append(x)
            # print(list)
        continue
# print("t'dah", list)
list.sort()
print('sorted', list)
