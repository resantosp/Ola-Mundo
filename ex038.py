n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
if n1 > n2:
    print('O MAIOR valor é o \033[1;40m {} \033[m'.format(n1))
elif n2 > n1:
    print('O MAIOR valor é o \033[1;40m {} \033[m'.format(n2))
else:
    print('Os valores \033[1;40m {} \033[m e \033[1;40m {} \033[m são IGUAIS'.format(n1, n2))


