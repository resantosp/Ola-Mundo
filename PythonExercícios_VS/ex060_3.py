print('-'*25, 'CALCULADORA DE FATORIAL', '-'*25, '\n')
n = int(input('Digite um número para calcular seu fatorial: '))

c = n
print('Calculando {}! = '.format(n), end='')
f = 1

for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
