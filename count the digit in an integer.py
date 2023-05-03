#program to count the digit in an integer
def countdigit(n):
    count = 0
    while n != 0:
        n//=10
        count += 1
    return count
n= int(input("enter the number : "))
print("number of digits : %d" %(countdigit(n)) )
