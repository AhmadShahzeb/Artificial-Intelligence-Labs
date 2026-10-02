# Stack function

stack = []

in_rnage = int(input("Give the range for Stack: "))
for i in range(in_rnage):
    x = int(input("Enter Value: "))
    stack.append(x)

print()
while stack:
    print(stack.pop(), end=" ")
