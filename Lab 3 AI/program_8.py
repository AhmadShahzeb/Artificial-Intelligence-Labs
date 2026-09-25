# print 1 to 6 , except 3, without using countinue statement

for i in range(1, 7):
    if i != 3:
        print(i, end=" ")


print("\n")
# another way

for i in range(1, 7):
    if i == 3:
        pass
    else:
        print(i, end=" ")