def factorial(n):
    result = n
    
    while n > 1:
        n = n - 1
        result = result * n
        
    return result
    
value = int(input('Digite valor: '))

#factorial(5)

print(factorial(value))