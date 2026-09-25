# fibonacci series

a = 1
b = 1
while a < 50:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

# fizz buzz

for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)