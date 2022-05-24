class Customer:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def print(self):
        print(f'Full name: {self.firstName} {self.lastName}')