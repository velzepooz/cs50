from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break

for i in range(height):

    for j in range(i + 1):
        for k in range(height - i - 1):
            print("_", end = "")
        print("#", end = "")

    print("")