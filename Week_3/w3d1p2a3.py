# Week 3> Day 1> Part 2> Activity 3

# Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 7 print “buzz”, if it’s divisible by both 3 and 7 print “fizzbuzz”.
# Otherwise print num.

str_num = input("Enter a number: ")
num = int(str_num)

if (num%3 == 0):
    print("fizz", end ="")
# using the end = "" argument allows us to print without a newline
if (num%7 ==0):
    print("buzz")