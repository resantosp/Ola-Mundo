print('========== SISTEMA DE REAJUSTE SALARIAL ==========')
antsal = float(input('Informe seu atual valor de salário: R$'))
porc = (15*antsal)/100
novsal = antsal+porc
print('Valor do salário atual: R${}'.format(antsal))
print('Valor do salário com reajuste de 15%: R${}'.format(novsal))
