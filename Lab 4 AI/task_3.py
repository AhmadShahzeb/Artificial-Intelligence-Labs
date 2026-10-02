# Binary Search Algorithm

arr = list(map(int, input("Enter numbers separated by space: ").split()))
# in_range = int(input("Give the range for the array: "))

# for i in range(in_range):
#     x = int(input("Enter Value: "))
#     arr.append(x)
arr.sort()
print(f"Array: {arr}")

target = int(input("Enter value to search: "))

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found != -1:
    print(f"Found at index {found}")
else:
    print("Not found")