"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome
do produto mais barato."""

print('-'*50)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-'*50)
total = plus1000 = 0
barato = ''
while True:
    name = input('Nome do produto: ')
    price = float(input('Preço: R$'))
    yesno = input('Quer continuar? [S/N] ').strip().upper()
    total += price
    if price > 1000:
        plus1000 += 1
    if barato == '':
        barato = name
        cheap = price
    elif price < cheap:
        cheap = price
        barato = name
    if yesno == 'N':
        break
print(f'''{" FIM DO PROGRAMA ":-^50}
O total da compra foi R${total:.2f}
Temos {plus1000} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${cheap:.2f}''')
