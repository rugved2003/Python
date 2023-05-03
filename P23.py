# hollow number pyramid pattern
size = 5
for i in range(size):
    # print spaces
    for j in range(size - i - 1):
        print(" ", end="")
    # print stars
    for k in range(2 * i + 1):
        if i == 0 or i == size - 1:
            print(k + 1, end="")
        else:
            if k == 0 or k == 2 * i:
                print(k + 1, end="")
            else:
                print(" ", end="")
    print()