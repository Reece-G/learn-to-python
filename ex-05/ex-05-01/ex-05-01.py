# Intialize variables 
count = 0 
total = 0 
average = 0 

# While function for reading user inputs until input reads "done".
while True: 
    inp = input("Enter a number: ")
    if inp == 'done': 
        break
    try: 
        finp = float(inp)
    except:
        print(inp)
        print("Invalid input.")
        continue
    count = count + 1
    total = total + finp 

#Using two variables count and total, calculate the average of the numbers provided by the user. 
if count > 1:
    average = total / count 

#Print the total, count and average variables back to the user. 
print(total, count, average)