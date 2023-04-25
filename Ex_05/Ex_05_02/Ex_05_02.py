number = None
highest = None
lowest = None

while number != 'done':
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = int(number)
    except:
        print('Invalid input')
        continue
    if highest is None:
        highest = number
        lowest = number
    else:
        if highest < number:
            highest = number
        if lowest > number:
            lowest = number

#Check for variables with useable values else end program with no output
if highest != None:
    print('Maximum is', highest)
    print('Minimum is', lowest)
else:
    quit()
