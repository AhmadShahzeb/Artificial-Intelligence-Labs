# Check if any value is same in both arrays
arr1 = [5,11,33,44,55]
length1 = (len(arr1))

arr2 = [1,2,3,4,5,6,8,22]
length2 = (len(arr2))

check = False
# Check for array 1
for i in range(length1):
    for j in range(length2):
        if arr1[i] == arr2[j]:
            print(f"{arr1[i]} is found same :")
            check = True

# Check if any same value is not found
if check == False:
    print("No similar value is found")


