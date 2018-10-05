# Write a loop that prompts the user to enter a series of pizza toppings
# Until they enter quit
# print message that you'll add that
topping = ""
while topping != "quit":
    topping = input("What kind of topping would you like? ")
    if topping != "quit":
        print('Adding ' + topping + ' to your pizza')
