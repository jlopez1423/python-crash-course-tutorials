def sandwiches(*fillings):
    print("\nThe following items have been added to you sandwich")
    for filling in fillings:
        print("- " + filling)


sandwiches('cheese', 'ham', 'lettuce')
sandwiches('pepperoni', 'cheese', 'lettuce', 'spinach', 'cucumbers')
sandwiches('cheese')