#Crie um programa que leia dois vaores mostre um menu na tela com somar, multiplicar, maior, novos números e sair do programa; seu programa deverá realizar a operação solicitada em cada caso

print('-'*20, 'Bem-vinde!', '-'*20)
p1 = int(input('Digite o primeiro valor: '))
p2 = int(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    print('\n')
    print('-'*20, 'SUAS OPÇÕES', '-'*20)
    print('\n[1] SOMAR\n[2] MULTIPLICAR\n[3] DESCOBRIR O MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n')
    opcao = int(input('O que gostaria de fazer? '))
    if opcao == 1:
        soma = p1 + p2
        print('A soma dos valores digitados é {}.'.format(soma))
    elif opcao == 2:
        mult = p1 * p2
        print('O produto dos valores digitados é {}.'.format(mult))
    elif opcao == 3:
        if p1 > p2:
            print('O maior valor digitado foi {}.'.format(p1))
        elif p2 > p1:
            print('O maior valor digitado foi {}.'.format(p2))
        else:
            print('Os valores digitados são iguais.')
    elif opcao == 4:
        print('Tudo bem! Informe os números novamente:')
        p1 = int(input('Digite o primeiro valor: '))
        p2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando... Até a próxima!')
    else:
        print('Ops! Parece que digitou errado. Observe atentamente as opções e tente novamente.')
print('-'*50)
