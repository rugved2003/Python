# right number triangle pattern
size = 5
for i in range(size):
    # print spaces
    for j in range(1, size - i):
        print(" ", end="")
    # print stars
    for k in range(i + 1):
        print(k + 1, end="")
    print()