# Divisible 7 and multiple 5

for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n, end=" ")