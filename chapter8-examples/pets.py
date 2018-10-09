def describe_pet(animal_type, pet_type):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_type.title() + ".")


describe_pet('hamster', 'hairy')
describe_pet('dog', 'willie')
