def computepay():
    # create variables and ask user for input.
    hrs = input("Enter your hours: ")
    pay = input("Enter your pay: ")

    # Try function to check inputs are numeric. Exception returns error message.
    try:
        fhrs = float(hrs)
        fpay = float(pay)
    except:
        print("Please enter a numeric value.")
        exit()

    # if statement to recognise when overtime has been accured and adjusts formula to account for that in end pay.
    if fhrs > 40:
        over = fhrs - 40
        gross = (fpay * (fhrs - over)) + (1.5 * fpay * over)
        print(fpay, fhrs, over)
    else:
        gross = fpay * fhrs 

    # Print result.
    print(gross)

computepay()
