class Users:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("Users Name: " + self.first_name + " " + self.last_name)
        print("Age: " + self.age)
        print("Email " + self.email)

    def greet_user(self):
        print("Welcome " + self.first_name + " " + self.last_name)


my_self = Users('Jose', 'Lopez', '26', 'jlopez@place.com')
my_self.describe_user()
my_self.greet_user()