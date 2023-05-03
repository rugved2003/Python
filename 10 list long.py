i = 10
list= []
while i>0:
    print("enter register number")
    num = input()
    list.append(num)
    i =i-1
print(list)
print()
#index
print("index")
print(list[1])
print()
#negative index
print("negative index")
print(list[-5])
print()
#range
print("range")
print(list[2:5])
print()
#before range valve
print("before range valve")
print(list[:2])
print()
#after range valve
print("after range valve")
print(list[5:])
print()
#change the item in list
print('change the item in list')
list[2] = "211"
print(list)
print()
#check if item exist
print("to check the item exist")
if "204" in list:
    print("yes 204 is the list")
else:
    print("no,204 is not in the list")
print()
#lenght of the list
print('lenght of the list')
print(len(list))
print()
#to add item to list
print("to add item to list")
list.append("250")
print(list)
print()
#to add an item to specifi index
print("to add an item to specifi index")
list.insert(3,"255")
print()

#sort the order tof the list
print("sort the order tof the list")
list.sort()
print(list)
print()
#reverse the list
print("reverse the list")
print(list)
print()
#to remove
print("to remove")
list.remove("206")
print()

#to delete list complelety
print("to delete list complelety")
del list
print()