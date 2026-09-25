# Classes and Objects

# Create class

class first_class:
    name = "ahmad"
    section = "IT"

x = first_class()
print(x.name)
print(x.section)

# Init function

class hello:
    def __init__(self, x, y):
        self.__name=x
        self.age=y
p1 = hello("Ahmad", 3)

print(p1.name)
print(p1.age)

# Object Methods

class hello:
    def __init__(self, x, y):
        self.name=x
        self.age=y

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = hello("Ahmad", 21)
p1.introduce()
