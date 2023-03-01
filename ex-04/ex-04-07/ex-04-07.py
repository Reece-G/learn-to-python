# Define function for computing the grade by asking for input and returning the grade as a string 
def computegrade():
    # Ask user for score input.
    inp = input("Enter a score: ")

    # Check the input as a numerical value.
    try:
        finp = float(inp)
    except:
        print("Error, please enter a score.")
        
    # Check the score inp against stored values and print result.
    if finp >= 0.9:
        print("A")
    elif finp >= 0.8:
        print("B")
    elif finp >= 0.7:
        print("C")
    elif finp >= 0.6:
        print("D")
    else:
        print("F")  


computegrade()
