primtermo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
for c in range(1, 11):
    c = primtermo + (c - 1) * razao
    print(c, end=' -> ')
print('FIM!')
