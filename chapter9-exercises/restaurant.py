class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, daily_count):
        self.number_served += daily_count

# Exercise 9-4
restaurant = Restaurant("Some Rest", "Chinese")
restaurant.set_number_served(5489)
restaurant.increment_number_served(89)
print("Number of customers served: " + str(restaurant.number_served))


my_restaurant = Restaurant("Jose's Tacos", "Mexican")
gingers_restaurant = Restaurant("Gingers Truffles", "Modern American")
serenas_fixings = Restaurant("Serenas fixings", "Fusion")


print("\nRestaurant name: " + my_restaurant.restaurant_name.title())
print("Restaurant type: " + my_restaurant.cuisine_type.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
gingers_restaurant.describe_restaurant()
gingers_restaurant.open_restaurant()
serenas_fixings.describe_restaurant()
serenas_fixings.open_restaurant()
