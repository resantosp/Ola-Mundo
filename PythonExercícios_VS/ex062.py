print('\n','-'*40, '\n', ' '*10, '= 10 TERMOS DA PA =', '\n', '-'*40)

ptermo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))

termo = ptermo
contador = 1 #o contador vai iniciar em 1 pq a ideia é ele contar quantos números já foram mostrados na tela até chegar em 10
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja exibir? '))
print('FIM!')
