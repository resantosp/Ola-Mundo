from math import hypot
print(('='*10), ' CÁLCULO DA HIPOTENUSA ', ('='*10))
coposto = float(input('Digite o valor do cateto opoto: '))
cadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(coposto, cadjacente)
print('Um triângulo retângulo com os seguintes valores: \n cateto oposto: {:>10} \n cateto adjacente: {:>10} \n terá valor de hipotenusa igual a {:>10}.'.format(coposto, cadjacente, hipotenusa))
