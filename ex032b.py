from datetime import date
ano = int(input('Informe um ano (XXXX) ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} informado É BISSEXTO'.format(ano))
else:
    print('\nO ano {} informado NÃO É BISSEXTO'.format(ano))
