hexNumbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

print(hexNumbers)

def hexToDec (hexNum):
    if len(hexNum) > 3:
        return None
    else:
    for char in hexNum:
        if char not in hexNumbers:
            print(rf'{char} is not a hex number!')
    
    print(hexNum[0])
    print(hexNum[1])
    print(hexNum[2])
    
    
            
            