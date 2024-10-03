# Week 3> Day 1> Part 2> Activity 5

# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is the same as the first.
# If it is return true, otherwise return false.

word = input("Enter a word: ")

if word[0] == word[len(word)-1]:
    print("True")
else:
    print("False")

