# Check if entered value is present in any of array
y = int(input("Enter a value to check: "))

arr1 = [1,2,3,4,5]
length1 = (len(arr1))

arr2 = [1,2,3,4,5,6,8,22]
length2 = (len(arr2))

# Check for array 1
for i in range(length1):
    if arr1[i] == y:
        print("Value found in array 1 at index:", i)

# Check for array 2
for i in range(length2):
    if arr2[i] == y:
        print("Value found in array 2 at index:", i)