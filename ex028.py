import random
from time import sleep
print(('='*5), ' Seja bem-vindo ao ADIVINHE O NÚMERO ', ('='*5))
nome = input('\nQual é o seu nome? ')
print('Olá, {}! Vamos começar? '.format(nome))
pc = random.randint(1, 5)
print('\nPENSANDO...')
sleep(3)
print('ESTOU PRONTO!')
n = int(input('\nEntre 1 e 5, em que número pensei?: '))
if n == pc:
    print('Na mosca! Você venceu o ADIVINHE O NÚMERO')
else:
    print('Não foi dessa vez! Você perdeu o ADIVINHE O NÚMERO')
print('O número correto era {:>10}'.format(pc))
