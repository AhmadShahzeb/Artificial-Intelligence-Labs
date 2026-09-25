# divisibe by 5

nums = input("Binary numbers: ").split(",")
result = []

for x in nums:
    if int(x, 2) % 5 == 0:
        result.append(x)

print(",".join(result))