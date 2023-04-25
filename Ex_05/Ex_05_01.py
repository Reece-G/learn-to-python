#Initialising the variables
number = None
count = 0
total = None

#Loop function
while number != 'done':
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
        count = count + 1
    except:
        print('Invalid input')
        continue
    if total == None:
        total = number
    else:
        total = total + number

#Check for variables with useable values else end program with no output
if count != 0:
    print(total, count, total / count)
else:
    quit()
