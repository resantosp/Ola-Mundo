n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print('\n \033[m')
print('O número total de valores DIVISÍVEIS por \033[1;40m{}\033[m no dado intervalo é: {}'.format(n, total))
if total != 2:
    print('O número \033[1;40m{}\033[m    === NÃO É PRIMO ===!'.format(n))
else:
    print('O número \033[1;40m{}\033[m    === É PRIMO! ==='.format(n))
