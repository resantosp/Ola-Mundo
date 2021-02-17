n = int(input('Digite um número: '))
print('\nO número escolhido foi \033[1;40m {} \033[m.'.format(n))
print('O que gostaria de fazer com o número escolhido?')
print('[1] para convertê-lo em BINÁRIO')
print('[2] para convertê-lo em OCTAL')
print('[3] para convertê-lo em HEXADECIMAL\n')
conversao = int(input('Sua opção:'))
if conversao == 1:
    print('O número \033[1;40m {} \033[m convertido para BINÁRIO é \033[1;40m {} \033[m'.format(n,bin(n)[2:]))
if conversao == 2:
    print('O número \033[1;40m {} \033[m convertido para OCTAL é \033[1;40m {} \033[m'.format(n, oct(n)[2:]))
if conversao == 3:
    print('O número \033[1;40m {} \033[m convertido para HEXADECIMAL é \033[1;40m {} \033[m'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')
