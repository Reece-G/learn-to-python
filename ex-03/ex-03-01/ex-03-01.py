# create variables and ask user for input.
hrs = input("Enter your hours: ")
pay = input("Enter your pay: ")

# convert string inputs to floats for calculation later.
fhrs = float(hrs)
fpay = float(pay)

# if statement to recognise when overtime has been accured and adjusts formula to account for that in end pay.
if fhrs > 40:
    over = fhrs - 40
    gross = (fpay * fhrs) + (1.5 * fpay * over)
else:
    gross = fpay * fhrs 

# Print result.
print(gross)
