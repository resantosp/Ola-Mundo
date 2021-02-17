from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento (XXXX): '))
alist = atual - nasc
if alist < 18:
    print('Faltam {} ano(s) para você se alistar.'.format((nasc + 18) - atual))
    print('Você deve se alistar em {}.'.format(nasc + 18))
elif alist > 18:
    print('Você EXCEDEU o prazo de alistamento em {} ano(s).'.format(atual - (nasc + 18)))
    print('Você deveria ter se alistado em {}'.format(nasc + 18))
else:
    print('Você deve se alistar IMEDIATAMENTE.')
    print('Seu prazo para se alistar é em {}'.format(nasc + 18))
