class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def hello(self):
        print("Hello my name is ", self.firstName, self.lastName)


class Admin(User):
    def superUser(self):
        print("Hello my name is admin")


user = User("Ulai", "Nava")
admin = Admin("Admin", "Admin")

user.hello()
user.firstName = "Sem"
user.hello()
# del user

admin.hello()
admin.superUser()