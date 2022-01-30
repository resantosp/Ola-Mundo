def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    # Write your code here
    if (operacao == '+'):
        resultado = numero + outroNumero
    elif (operacao == '-'):
        resultado = numero - outroNumero
    else:
        resultado = 0

    return resultado


calculadoraAdicaoSubtracao(5, 4, '+')


def tripleTheChances(chances):
    array = []
    for i in range(len(chances)):
        x = chances[i]
        x = x * 3
        array.append(x)

    return array


tripleTheChances([2, 3, 5, 8, 10])

def vezesLetraAparece(frase, letra):
    # Write your code here
    n = 0
    lista = list(frase)
    for i in range(len(lista)):
        if lista[i] == letra:
            n += 1
    return n

vezesLetraAparece('The Lord of The Rings', 'o')