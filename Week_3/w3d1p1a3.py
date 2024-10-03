# A shop sells apples for 25p per apple, and bananas for 50p per banana.
# Create a program which asks a user how many apples they want to buy, and how many bananas they want to buy.
# Display the total cost of the apples, the total cost of the bananas.

# 10 apples would cost £2.50
# Your program will say £2.5
# Research how to have your answer formatted to have two decimal places.

apple_price = .25
banana_price = .5

print(f"Apples cost {apple_price}p each and bananas cost {banana_price}p each. ")
str_number_of_apples = input("How many apples would you like to buy?")
str_number_of_bananas = input("How many bananas would you like to buy?")
number_of_apples = int(str_number_of_apples)
total_cost_of_apples = number_of_apples*.25
number_of_bananas = int(str_number_of_bananas)
total_cost_of_bananas = number_of_bananas*.5

total_cost = total_cost_of_apples + total_cost_of_bananas
print(f"The total cost of apples is £{total_cost_of_apples:.2f} and The total cost of bananas is £{total_cost_of_bananas:.2f}. The combined cost is £{total_cost:.2f}" )