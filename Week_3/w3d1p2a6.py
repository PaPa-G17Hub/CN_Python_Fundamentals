# Week 3> Day 1> Part 2> Activity 6

# Create a variable called word that takes a string.
# Create an if statement that checks if the whole string is a palindrome (reads the same forwards as it does backwards e.g. abba)

# method 1: using recursion
# def isPalindrome(s):
#     return s == s[::-1]

# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)

# if ans:
#     print("Yes")
# else:
#     print("No")

# method 2: Martin's code
test_txt = input('Enter text')
 
palindrome = False
for i in range(0, len(test_txt) // 2):
  palindrome = test_txt[i] == test_txt[0 - (i + 1)]
  if not palindrome:
      break
 
if palindrome:
    print(test_txt + ' is a palindrome')
else:
    print(test_txt + ' is not a palindrome')