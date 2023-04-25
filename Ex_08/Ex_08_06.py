# Creating list
list = []


# Loop for appending list until user inputs 'done'.
while True:
    inp = input('Enter a number please: ')
    # print('input', inp)
    if inp == 'done':
        break
    try:
        inp = float(inp)
    except:
        continue
    list.append(inp)
    continue

# max / min functions

print(max(list))
print(min(list))
# print('Maximum:', max,'\nMinimum:', min)
