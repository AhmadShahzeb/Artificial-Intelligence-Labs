# Functions

# Calling the function

def first():
    print("Function calling")

x = 1
if x==1:
    first()

# Passing parameters

def fun(name):
    print("Hello" +" "+  name)

fun("Ahmad")

# Default parameters

def default(name="Ahmad"):
    print("Hello" +" "+  name)

default()
default("Hello")

# Passing Lists

def lists(count):
    for x in count:
        print(x)


list = ["first", "second", "third"]
lists(list)

# Return values

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# keyword arguments

def keyword(name, age):
    print(f"Hello {name}, your age is {age}")

keyword("Ahmad", age=21)   
