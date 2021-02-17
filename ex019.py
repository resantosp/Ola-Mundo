import random
print(('='*10), ' SORTEADOR DE NOME ', ('='*10))
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
seq = a1, a2, a3, a4
print('O aluno escolhido é: {:>10}.'.format(random.choice(seq)))
