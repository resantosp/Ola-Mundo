from random import randint
print(('='*10), 'Rock Paper Scissors Lizard Spock', ('='*10))
print('\nSuas opções:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
print('[4] LAGARTO')
print('[5] SPOCK')
jogador = int(input('Qual é a sua jogada? '))
pc = randint(1, 5)
print('\nJOGADOR 1 escolhe: {}'.format(jogador))
print('JOGADOR 2 escolhe: {}'.format(pc))
print(' ')
if jogador == 1:
    if pc == 1:
        print('EMPATE!')
    elif pc == 2:
        print('Papel cobre pedra. PC venceu!')
    elif pc == 3:
        print('Pedra amassa tesoura. VOCÊ venceu!')
    elif pc == 4:
        print('Pedra esmaga lagarto. VOCÊ venceu!')
    else:
        print('Spock vaporiza pedra. PC venceu!')
if jogador == 2:
    if pc == 1:
        print('Papel cobre pedra. VOCÊ venceu!')
    elif pc == 2:
        print('EMPATE!')
    elif pc == 3:
        print('Tesoura corta papel. PC venceu!')
    elif pc == 4:
        print('Lagarto come papel. PC venceu!')
    else:
        print('Papel refuta Spock. VOCÊ venceu!')
if jogador == 3:
    if pc == 1:
        print('Pedra esmaga tesoura. PC venceu!')
    elif pc == 2:
        print('Tesoura corta papel. VOCÊ venceu!')
    elif pc == 3:
        print('EMPATE!')
    elif pc == 4:
        print('Tesoura decapta lagarto. VOCÊ venceu!')
    else:
        print('Spock derrete tesoura. PC venceu!')
if jogador == 4:
    if pc == 1:
        print('Pedra esmaga lagarto. PC venceu!')
    elif pc == 2:
        print('Lagarto come papel. VOCÊ venceu!')
    elif pc == 3:
        print('Tesoura decapta lagarto! PC venceu!')
    elif pc == 4:
        print('EMPATE!')
    else:
        print('Lagarto envenena Spock. VOCÊ venceu!')
if jogador == 5:
    if pc == 1:
        print('Spock vaporiza pedra. VOCÊ venceu!')
    elif pc == 2:
        print('Papel refuta Spock. PC venceu!')
    elif pc == 3:
        print('Spock derrete tesoura. VOCÊ!')
    elif pc == 4:
        print('Lagarto envenena Spock. PC venceu!')
    else:
        print('EMPATE!')
