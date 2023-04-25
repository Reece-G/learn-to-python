fhand = open('text.txt')
count = 0

for line in fhand:
    words = line.lower().split()
    # print('Debug:', words)

    # Guardian pattern written in compund to conditional ignore of lines.
    if len(words) < 3 or words[0] != 'from' : continue
    print(words[2])
