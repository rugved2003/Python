def countdigit(n):
    if n == 0:

      return 0
    return 1 + countdigit(n//10)
n= int(input("enter the number : "))
print("number of digits : %d" %(countdigit(n)) )