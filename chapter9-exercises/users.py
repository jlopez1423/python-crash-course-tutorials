class Users:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("Users Name: " + self.first_name + " " + self.last_name)
        print("Age: " + self.age)
        print("Email " + self.email)

    def greet_user(self):
        print("Welcome " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_self = Users('Jose', 'Lopez', '26', 'jlopez@place.com')
my_self.describe_user()
my_self.greet_user()
my_self.increment_login_attempts()
my_self.increment_login_attempts()
my_self.increment_login_attempts()
my_self.increment_login_attempts()
my_self.increment_login_attempts()
print("Amount of login attempts: " + str(my_self.login_attempts))
my_self.reset_login_attempts()
print("Amount of login attempts: " + str(my_self.login_attempts))