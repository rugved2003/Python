import array as arr
newarray = arr.array('d', [4.5, 6.5, 3.9, 8.7, 3.3, 7.7])
print("First element:", newarray[0])
print("Second element:", newarray[1])
print("Last element:", newarray[-1])
print(newarray[2:5]) # 3rd to 5th
print(newarray[:])   # beginning to end