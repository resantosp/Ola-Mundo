media = 0
idadevelho = 0
mulheres = 0
somaidade = 0

for p in range(1, 5):
    print("="*5, "{}ª PESSOA".format(p), "="*5)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        idadevelho = idade
        nomevelho = nome
    else:
        if sexo in "Mm":
            if idade > idadevelho:
                idadevelho = idade
                nomevelho = nome
        if sexo in "Ff":
            if idade < 20:
                mulheres += 1

media = somaidade / 4
print("\n")
print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(idadevelho, nomevelho))
print("Ao todo há {} menina(s) com menos de 20 anos no grupo.".format(mulheres))
