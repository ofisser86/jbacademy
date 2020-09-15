class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def great(self):
        return f"Hello, I am {self.name}!"


pr = Person(input())
print(pr.great())
