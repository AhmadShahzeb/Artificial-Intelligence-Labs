# input lines and output them

while True:
    line = input("Write something: ")
    if line == "":
        break
    print(line.lower())