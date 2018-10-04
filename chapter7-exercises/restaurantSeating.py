# Write a program that asks the user how many people are in their dinner group
amount_people = input("How many people in your group tonight? ")
# If the answer is more than eight
if int(amount_people) > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")
