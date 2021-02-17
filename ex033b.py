pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
tv = int(input('Terceiro valor: '))
menor = pv
if sv <= pv and sv <= tv:
    menor = sv
if tv <= pv and tv <= sv:
    menor = tv
maior = pv
if sv >= pv and sv >= tv:
    maior = sv
if tv >= pv and tv >= sv:
    maior = tv
print('MENOR valor inserido: {}'.format(menor))
print('MAIOR valor inserido: {}'.format(maior))

###primeiro = int(input('Digite o primeiro número:'))
# segundo = int(input('Digite o segundo número:'))
# terceiro = int(input('Digite o terceiro número:'))
# numeros = [primeiro, segundo, terceiro]
# print('O maior valor digitado foi {}'.format(max(numeros)))
# print('O menor numero digitado foi {}'.format(min(numeros)))
