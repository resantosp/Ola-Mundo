print('=========== TABUADA ===========')
n = int(input('Digite um valor inteiro: '))
print('========', 'TABUADA DE {}'.format(n),'=========')
for c in range(1, 11):
    produto = n * c
    print('{} * {} = {}'.format(n, c, produto))
print('FIM!')
