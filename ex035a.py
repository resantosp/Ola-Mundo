from time import sleep
print(('='*10), '\033[1;40mSISTEMA DE EMPRÉSTIMO\033[m', ('='*10))
nome = input('Nome completo do contratante: ')
print('\nOlá, {}. Vamos analisar seu pedido de financiamento.'.format(nome.upper()))
valor = float(input('Valor do imóvel: '))
salario = float(input('Valor do seu salário atual: '))
anos = int(input('Tempo para quitar (anos): '))
meses = anos * 12
print('\nPROCESSANDO...')
sleep(3)
prestacao = valor / meses
porcent = (30 * salario) / 100
print('\nValor máximo de prestação: R${:.2f}.'.format(porcent))
print('Valor da prestação desejada: R${:.2f}.'.format(prestacao))
if prestacao > porcent:
    print('\033[1;40mFINANCIAMENTO NEGADO\033[m')
    print('Sentimos muito e esperamos te ver novamente!')
elif prestacao == porcent:
    print('FINANCIAMENTO APROVADO')
    print('Contudo, precisaremos de mais algumas documentações para fechar o contrato.')
    print('Entre em contato pelo número: 0444')
else:
    print('\033[1;40mFINANCIAMENTO APROVADO\033[m')
    print('Entre em contato pelo número: 0444')
print('\nAgradecemos a preferência. \nAtt ADMINISTRAÇÃO')
