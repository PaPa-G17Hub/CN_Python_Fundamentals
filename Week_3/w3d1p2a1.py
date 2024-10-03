# Week 3> Day 1> Part 2> Activity 1

# Create a variable called password.
# Check how many letters are in the password, if there are fewer than 8 print that the password is too short.
# Otherwise print the password.

password = input("Enter a password? ")
if (len(password) < 8):
    print("The password is too short")
else:
    print(f"Passowrd is {password}")