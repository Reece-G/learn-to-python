# Create variable asking user for input.
inp = input("Enter a temperature in Celsius: ")

# Convert string variable inp to float type.
finp = float(inp)

# Calculate the temperature into Fahrenheit and print result.
f = (finp * 9/5) + 32 
print("Temperature in Fahrenheit:", f)