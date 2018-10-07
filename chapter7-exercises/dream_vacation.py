responses = {}

polling = True

while polling:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to visit? ")

    responses[name] = response

    repeat = input("Would you like to continue? Yes/No ")

    if repeat == 'no':
        polling = False

for name, response in responses.items():
    print(name + " would like to go to " + response)