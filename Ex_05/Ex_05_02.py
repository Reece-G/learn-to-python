#Initialising the variables
number = None
total = None
highest = None
lowest = None

#Loop function
while number != 'done':
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Invalid input')
        continue
    if total == None:
        total = number
        highest = number
        lowest = number
    else:
        total = total + number
        if highest < number:
            highest = number
        if lowest > number:
            lowest = number

#Check for variables with useable values else end program with no output
if total != None:
    print(total, highest, lowest)
else:
    quit()
