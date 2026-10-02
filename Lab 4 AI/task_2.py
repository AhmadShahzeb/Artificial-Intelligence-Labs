# Stack function

# stack = []

# def push(value):
#     stack.append(value)

# in_rnage = int(input("Give the range for Stack: "))
# for i in range(in_rnage):
#     x = input("Enter Value: ")
#     push(x)

# print()
# while stack:
#     print(stack.pop(), end=" ")


# Method 2

stack = []

def push(value):
    stack.append(value)

def pop(stack):
    if len(stack) == 0:
        print("No value in stack: ")
    else:
        print(stack.pop(), end=" ")


push(55)
push(10)
push(5)

print(stack)

pop(stack)
pop(stack)
pop(stack)