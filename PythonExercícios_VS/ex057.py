#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter o valor correto.

s = 'F'

while s != 'F':
    s = str(input('Sexo: [F/M] ')).upper()
    if s == 'F' or s == 'M':
        print('Obrigada.')
    else:
        print('Por favor, insira corretamente.')
print('Obrigada.')
