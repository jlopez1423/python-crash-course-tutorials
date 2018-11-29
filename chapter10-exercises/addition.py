num1 = input("Please enter the first number to add: ")
num2 = input("Please enter the second number to add: ")

try:
    print(int(num1) + int(num2))
except ValueError:
    print("You can't add a text value!")