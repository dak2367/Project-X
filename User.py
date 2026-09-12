class User:
    def __init__(self, username):
        self.username = username

    def createUser(self):
        self.username = input("Please enter a username")
        self.password = input("Please enter a password")

