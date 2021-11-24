#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('\n','-'*40, '\n', ' '*10, '= CALCULADORA DE PA =', '\n', '-'*40)

ptermo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))

final = ptermo + ((10 - 1) * razao)

while ptermo <= final:
    print('{} ->'.format(ptermo), end=' ')
    ptermo += razao
print('ACABOU!')

#print(final)
