class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")


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
