# cross pattern in python
size = 6
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()