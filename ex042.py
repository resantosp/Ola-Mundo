r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar triângulo!')
    if r1 == r2 and r2 == r3:
        print('O triângulo será EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo será ISÓSCELES')
    else:
        print('O triângulo será ESCALENO')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')