# Python3 program to convert Hexadecimal number to Binary
def to4DigitBin(value):
    return '0'*(4-len(value))+value
def HexadecimalToBinary(Hexadecimal):
    resultBinary = '' # Initialize Empty string

    for eachElement in Hexadecimal:
        if(eachElement.isdigit()):
            binaryOfSingleDigit = bin(int(eachElement))[2:]
            resultBinary += to4DigitBin(binaryOfSingleDigit)
 
        elif(eachElement.isalpha() and ord(eachElement) < 71):
            resultBinary += to4DigitBin(bin(ord(eachElement)-55)[2:])

        else:            
            resultBinary = 'Invalid hexadecimal digit: ' + eachElement
            break

    return 'Equivalent Binary value is: '+ resultBinary

Hexadecimal = '12FD'   # input('Enter Hexadecimal: ')

print(HexadecimalToBinary(Hexadecimal))