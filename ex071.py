print('='*30)
print('{: ^30}'.format('BANCO CENTRAL'))
print('='*30)
saque = int(input('Valor de saque: R$'))
total = saque
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CENTRAL! Tenha um bom dia!')