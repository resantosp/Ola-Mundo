#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter o valor correto.

sexo = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [F/M] ')).upper().strip()[0]

idade = int(input('Informe sua idade:'))
