# alphabet diamond pattern
size = 5
alpha = 65
num = 0

# upside pyramid
for i in range(1, size + 1):
    # printing spaces
    for j in range(size, i - 1, -1):
        print(" ", end="")
    # printing alphabets
    for k in range(0, i * 2 - 1):
        print(chr(alpha + num), end="")
        num += 1
    num = 0
    print()
#downward pyramid
for i in range(1, size):
    # printing spaces
    for j in range(0, i+1):
        print(" ", end="")
    # printing alphabets
    for k in range((size - i) * 2 - 1):
        print(chr(alpha + num), end="")
        num += 1
    num = 0
    print()