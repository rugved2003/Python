# reverse pyramid pattern
n = 6

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()