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


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privileges in self.privileges:
            print(privileges)


class Admin(Users):

    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(privileges)


user_privileges = ['can write blog', 'can delete blog', 'can add content', 'can delete content']
me_admin = Admin("Jose", "Lopez", 27, "jlopez@me.com", user_privileges)
me_admin.privileges.show_privileges()
