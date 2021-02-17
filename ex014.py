print(('='*10), ' CONVERSOR DE TEMPERATURA ', ('='*10))
c = float(input('Insira o valor da temperatura em graus Celcius: '))
f = (c*1.8)+32
print('O valor de {}ºC convertido para Fahrenheit é: '.format(c))
valorfinal = str('{}F'.format(f))
print('{:^45}'.format(valorfinal))
