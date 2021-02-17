print(('-=-'*7), ' SISTEMA RADAR DIGITAL ', ('-=-'*7))
vel = float(input('\nQual é a velocidade atual do carro? '))
multa = (vel - 80)*7
if vel <= 80:
    print('\nTenha um bom dia! Dirija com segurança.')
else:
    print('\nVOCÊ EXCEDEU A VELOCIDADE MÁXIMA DE SEGURANÇA')
    print('Valor da Multa: R${}.'.format(multa))
    print('Tenha um bom dia! Dirija com segurança.')
print('Att. RD')