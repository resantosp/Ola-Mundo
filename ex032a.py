ano = int(input('Informe um ano (XXXX): '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('\nO ano {} informado É BISSEXTO'.format(ano))
    else:
        if ano % 400 == 0:
            print('\nO ano {} informado É BISSEXTO'.format(ano))
        else:
            print('\nO ano {} informado NÃO É BISSEXTO'.format(ano))
else:
    if ano % 400 == 0:
        print('\nO ano {} informado É BISSEXTO'.format(ano))
    else:
        print('\nO ano {} informado NÃO É BISSEXTO'.format(ano))
