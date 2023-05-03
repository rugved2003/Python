n= int(input("enter n numbers :"))
odd=0
even=0
for i in range(1,n):
    if(i%2==0):
        even+=1

    else:
        odd+=1
print("total number of even numbers are",even)
print("total number of odd numbers are",odd)