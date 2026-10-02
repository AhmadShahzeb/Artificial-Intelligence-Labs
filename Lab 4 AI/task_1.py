# queue function

queue = []

in_rnage = int(input("Give the range for Queue: "))
for i in range(in_rnage):
    x = int(input("Enter Value: "))
    queue.append(x)

print()
while queue:
    print(queue.pop(0), end=" ")