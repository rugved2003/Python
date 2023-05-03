COST_OF_PRODUCT= int(input("Enter the MRP of item to be purchased:"))
CGST= COST_OF_PRODUCT*0.09
SGST = COST_OF_PRODUCT *0.09
TOTAL = COST_OF_PRODUCT+ CGST + SGST
print("The total price of the item inclusive of all taxes is: ",TOTAL)