# # queue function

# queue = []

# def push(value):
#     queue.append(value)


# in_rnage = int(input("Give the range for Queue: "))

# for i in range(in_rnage):
#     x = input("Enter Value: ")
#     push()

# print()
# while queue:
#     print(queue.pop(0), end=" ")

# 2nd method

queue = []

def push(value):
    queue.append(value)

def pop(queue):
    if len(queue) == 0:
        print("NO value in queue: ")
    else:
        print(queue.pop(0), end = " ")

push(55)
print(queue)
push(10)
print(queue)
push(4)
print(queue)
pop(queue)
print()
print(queue)
pop(queue)
print()
print(queue)
pop(queue)


