maior = 0
menor = 0

for pessoas in range(1, 5):
    peso = float(input("Peso da {} pessoa (kg): ".format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("\n")
print("O maior peso inserido foi {}kg.".format(maior))          
print("O menor peso inserido foi {}kg.".format(menor))
