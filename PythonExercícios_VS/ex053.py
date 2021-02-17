from time import sleep
print(('=')*10, 'PALÍNDROMO', ('=')*10)
usuario = input('Digite uma frase: ').replace(' ', '').upper()
invertido = ''
for letra in range(len(usuario) - 1, -1, -1):
    invertido = invertido + usuario[letra]
print('INVERTENDO...')
sleep(1)
print('A frase {} invertida é {}.'.format(usuario, invertido))
if usuario == invertido:
    print('TEMOS UM \033[40mPALÍNDROMO\033[m!')
else:
    print('A FRASE DIGITADA \033[40mNÃO É UM PALÍNDROMO\033[m')
