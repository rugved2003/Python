# hollow square pattern
size = 5
for i in range(size):
    # print star in first and last row
    if i == 0 or i == size - 1:
        print('*' * size)
    else:
        # print * in first and last position in other rows
        print('*' + ' ' * (size - 2) + '*')