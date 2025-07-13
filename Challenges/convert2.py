from decimal import Decimal, getcontext
hexNumbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
#print(hexNumbers)

def hexToDec (hexNum):
    char = hexNumbers()
    
    if len(hexNum) > 3:
        return None
    if char not in hexNumbers:
        print('Is not a hex number!')
    else:
        for char in hexNum:
            print(hexNum.decode(char, 'base16'))
            #print(char.decode(hexNum, 'utf-16'))
            #print(hexNum[0])
            #print(hexNum[1])
            #print(hexNum[2])

hexNum = input('Digite um número hexadecimal: ').upper()

hexToDec(hexNum)

print(hexToDec(hexNum))

            
            