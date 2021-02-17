print(('-=-'*7), ' SISTEMA 1001 ', ('-=-'*7))
print('\n')
print(('-'*8), 'TABELA DE DISTÂNCIA', ('-'*8))
print('Rio de Janeiro -> São Paulo {:>10}'.format(357))
print('Rio de Janeiro -> Belo Horizonte {:>5}'.format(352))
print('-'*37)
distancia = int(input('\nDistância da sua viagem: '))
if distancia <= 355:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('VALOR DA PASSAGEM: {:>10}'.format(preco))
print('\nAgradecemos a preferência.')
print('Att. Administração 1001')
