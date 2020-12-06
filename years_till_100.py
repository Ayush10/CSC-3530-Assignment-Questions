# Program to calculate when a person will turn 100 years old
# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating the time remaining
time = (2020 - age) + 100

# Displaying the result
print("{0} will be 100 years old in the year {1}.".format(name, str(time)))
