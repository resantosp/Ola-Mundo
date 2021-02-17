nome = input('Qual é o seu nome completo?\n').upper().strip().split()
print('É você {} {} ?\n'.format(nome[0], nome[len(nome)-1]))
