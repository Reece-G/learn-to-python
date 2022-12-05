# create variables and ask user for input.
hrs = input("Enter your hours: ")
pay = input("Enter your pay: ")

# convert string inputs to floats for calculation later.
fhrs = float(hrs)
fpay = float(pay)

#calculate gross pay and print.
gross = fpay * fhrs 
print(gross)
