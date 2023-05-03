# List indexing
my_list = ['r', 'u', 'g', 'v', 'e', 'd']
# Output: r
print(my_list[0])
# Output: g
print(my_list[2])
# Output: e
print(my_list[4])
# Nested List
n_list = ["Happy", [2, 0, 1, 5]]
# Nested indexing
print(n_list[0][1])
print(n_list[1][3])
# Error! Only integer can be used for indexing
print(my_list[4.0])