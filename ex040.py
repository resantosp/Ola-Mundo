n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('A média do aluno é {}.'.format(media))
    print('O aluno está REPROVADO')
elif media >= 5 and media < 7:
    print('A média do aluno é {}.'.format(media))
    print('O aluno está EM RECUPERAÇÃO')
else:
    print('A média do aluno é {}.'.format(media))
    print('O aluno está APROVADO')
