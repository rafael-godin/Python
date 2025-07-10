A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
hexadecimal = [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]
hex_str = 'hexNum'

def convert_to_decimal(hex_num):
    decimal_value = 0
    for i, digit in enumerate(reversed(hex_num)):
        decimal_value += hexadecimal.index(digit) * (16 ** i)
    return decimal_value
if hex_str == 'hexNum':
    print('It is a hexadecimal number')
else:
    print(None)
    
Resposta = hex_str(input('Aguardando valor: '))

convert_to_decimal(Resposta)

print(convert_to_decimal(Resposta))
    
    