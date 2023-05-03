# Python program explaining
# numpy.concatenate() function
# importing numpy as new
import numpy as new

arr1 = new.array([[2, 4], [6, 8]])
arr2 = new.array([[3, 5], [7, 9]])
print("for axis =0")
#axis=0
a = new.concatenate((arr1, arr2), axis=0)
print(a)
print("--------------------------------")
#axis=1
print("for axis =1")
b = new.concatenate((arr1, arr2), axis=1)
print(b)
print("--------------------------------")
#axis = none
c = new.concatenate((arr1, arr2), axis=None)
print("for axis none")
print(c)

