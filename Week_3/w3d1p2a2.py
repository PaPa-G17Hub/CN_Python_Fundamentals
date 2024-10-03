# Week 3> Day 1> Part 2> Activity 2

# Create a variable called num.
# Check if the variable is divisible by 3 or 5.
# If it is print “This number is divisible by 3 or 5” to the terminal.
# Otherwise print “This number is not divisible by 3 or 5”.

str_num = input("Enter a number: ")
num = int(str_num)

if (num%3 == 0) or (num%5 == 0):
    print(f"{num} is divisible by 3 or 5")
else:
    print(f"{num} is not divisible by 3 or 5")