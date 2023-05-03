#values(letter,number,string)
#data types(numbers,sets,sequesnces,dictionary)
a=(4,"air",8.56,[8,3,9],(2,3),{"no":45,"class":13,"age":17} ,{8.56,"cup"})
print(type(a[0]),type(a[1]),type(a[2]),type(a[3]),type(a[4]),type(a[5]),type(a[6]))
#date type boolean

print(a[2]>a[0])
##key words(if,elif,else,and not ,true,false,for break,print)
if (a[0]>6):
    print("yes it is greater than 6")
elif(a[0]==0):
    print("yes it is equal to zero")
else:
    print("yes it is less than 6")
print(a[0]and a[2])
print(a[0]or a[2])
print(not a[1])
for i in range(2,5):
    c=2*i
    print(c)
