n = int(input('Digite um número: '))
fatorial = 1
x = 2

while x <= n:
    fatorial = fatorial * x
    x = x + 1
print('O fatorial de {} é {}.'.format(n, fatorial))

#from math import factorial
