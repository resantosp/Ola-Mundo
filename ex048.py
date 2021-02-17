##calcule a soma entre TODOS os números ímpares E múltiplos de 3 entre 1 e 500
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('A soma dos {} valores vale {}'.format(contador, soma))
print('FIM!')
