# number diamond pattern
size = 5
num = 1

# upside pyramid
for i in range(1, size + 1):
    # printing spaces
    for j in range(size, i - 1, -1):
        print(" ", end="")
    # printing star
    for k in range(0, i * 2 - 1):
        print(num, end="")
        num += 1
    # set the number to 1
    num = 1
    print()
# downside pyramid
for i in range(1, size):
    # printing spaces
    for j in range(0, i+1):
        print(" ", end="")
    # printing star
    for k in range((size - i) * 2 - 1):
        print(num, end="")
        num += 1
    # set num to 1
    num = 1
    print()