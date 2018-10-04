# Ask user for a number
number = input("Please enter a number: ")

# report if multiple of ten
if int(number) % 10 == 0:
    print("Is multiple of ten.")
else:
    print("Not multiple of ten.")