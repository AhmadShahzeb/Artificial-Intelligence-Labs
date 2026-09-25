# calculate number of digits and letters

s = input("String: ")
d = l = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        l += 1
print("Letters", l)
print("Digits", d)