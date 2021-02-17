from datetime import date
nasc = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('A idade é {} e a categoria será MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('A idade é {} e a categoria será INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('A idade é {} e a categoria será JÚNIOR'.format(idade))
else:
    print('A idade é {} e a categoria será SÊNIOR'.format(idade))
