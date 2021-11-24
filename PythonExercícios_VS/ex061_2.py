print('\n','-'*40, '\n', ' '*10, '= 10 TERMOS DA PA =', '\n', '-'*40)

ptermo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))

termo = ptermo
contador = 1 #o contador vai iniciar em um pq a ideia é ele contar quandos números já foram mostrados na tela até chegar em 10

while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    contador += 1
print('ACABOU!')
