import emoji
import math
from time import sleep
from math import ceil
print(('='*15), emoji.emojize('\033[1;40mSEU PRIMEIRO MILHÃO\033[1;33;40m:corn:\033[m', use_aliases=True), ('='*15))
nome = input('Nome: ')
print('\nOlá, \033[1;33m{}\033[m. \nVamos analisar quanto tempo você levará para ter o seu primeiro milhão.'.format(nome.upper()))
capinicial = float(input('Capital inicial: '))
aportemensal = float(input('Aporte mensal: '))
juros = float(input('Taxa de rendimento mensal (%): '))
taxa = (juros / 100) + 1
montante = 1000000
##passo1 = (aportemensal / taxa) - montante
##passo2 = (aportemensal / taxa) + capinicial
##passo3 = math.log(passo1, 10) - math.log(passo2, 10)
##tempo = passo3 / math.log(taxa, 10)
tempo = math.log(((aportemensal / taxa - montante) / (aportemensal / taxa + capinicial)), 10) / math.log(taxa, 10)
meses = tempo*12
print('\nPROCESSANDO...')
sleep(2)
print('\nVocê levará \033[1;33m{}\033[m meses ou \033[1;33m{}\033[m anos para garantir seu primeiro milhão!'.format(ceil(meses), ceil(tempo)))
## problema: e o investimento mensal?