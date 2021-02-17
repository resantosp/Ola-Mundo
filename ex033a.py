pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
tv = int(input('Terceiro valor: '))
if pv > sv and pv > tv:
    print('O MAIOR valor inserido foi: {}'.format(pv))
if sv > pv and sv > tv:
    print('O MAIOR valor inserido foi: {}'.format(sv))
if tv > sv and tv > pv:
    print('O MAIOR valor inserido foi: {}'.format(tv))
if pv < sv and pv < tv:
    print('O MENOR valor inserido foi: {}'.format(pv))
if sv < pv and sv < tv:
    print('O MENOR valor inserido foi: {}'.format(sv))
if tv < sv and tv < pv:
    print('O MENOR valor inserido foi: {}'.format(tv))
