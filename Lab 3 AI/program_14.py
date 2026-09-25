# password check

p = input("Password: ")
up = low = num = sym = False
for ch in p:
    if ch.isupper(): 
        up = True
    elif ch.islower(): 
        low = True
    elif ch.isdigit(): 
        num = True
    elif ch in "$#@": 
        sym = True

if up and low and num and sym and 6 <= len(p) <= 16:
    print("Valid password")
else:
    print("Invalid password")