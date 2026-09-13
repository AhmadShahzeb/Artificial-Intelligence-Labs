y = int(input("Enter a value: "))

arr = [1,2,3,4,5]
length = (len(arr))
check = False

for i in range(length):
    if arr[i] == y:
        print("Value found at index:", i)
        check = True

if check == False:
    print("Value not found")