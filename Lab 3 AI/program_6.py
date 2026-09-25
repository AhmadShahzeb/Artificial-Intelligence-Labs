# Number of even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
for n in numbers:
    if n%2==0:
        even += 1
print("Number of even numbers: ", even, "Number of odd numbers: ", len(numbers) - even)