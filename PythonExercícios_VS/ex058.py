#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint

print('Olá! Sou seu computador e vou pensar em um número entre 0 e 10.')
sleep(1)
print('Pensando...')
sleep(2)
pc = randint(1, 11)
print('Pensei! Será que você consegue adivinhar qual número foi?')
palpite = int(input('\nQual é o seu palpite? '))

n = 1

if palpite == pc:
    print('\nUauu.. Você é um gênio da legilimência! Acertou na primeira tentativa!')
else:
    while palpite != pc:
        palpite = int(input('Uuuuh.. você errou, amigo. Dê um novo palpite: '))
        n += 1
    print('\nUauu! Você sabe mesmo ler mentes! Acertou em {} tentativas.'.format(n))

'''Quero fazer de um jeito que vai dar para o abençoado que tá jogando decidir se quer jogar novamente ou não
jog_nov = str(input('Adorei jogar com você! Quer jogar novamente? [S/N]').upper().strip()[0]
'''
