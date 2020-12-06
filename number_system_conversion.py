# Program to convert Decimal Number Systems to Other Number Systems
# Taking user input
dec = int(input("Enter decimal numbers for conversion: "))

# Displaying the results
print("The given number in decimal number system is {0}.".format(str(dec)))
print("The given number in binary number system is {0}.".format(str(bin(dec))))
print("The given number in octal number system is {0}.".format(str(oct(dec))))
print("The given number in hexadecimal number system is {0}.".format(str(hex(dec))))
