# Week 3> Day 1> Part 2> Activity 4

# Correct the code on the following slide so it functions as expected.
# Can you use anything to make sure “London” and “london” are accepted as correct answers?

print("What is the capital of England?" )

answer = input("Type your answer here >> ")

if answer.lower() == "london":
    print(f"Correct! The answer is {answer.capitalize()}" )
else:
    print(f"Incorrect, the answer is 'London', not {answer}" )