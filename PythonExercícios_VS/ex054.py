from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = (int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoa))))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print("\n")
print("Ao todo tivemos {} pessoa(s) maior(es) de idade.".format(totalmaior))
print("Ao todo tivemos {} pessoa(s) menor(es) de idade.".format(totalmenor))        
