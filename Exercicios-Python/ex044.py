price = float(input('Preço das compras: R$'))
opc = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? """))
if opc == 1:
    final = price - price*10/100
elif opc == 2:
    final = price - price*5/100
elif opc == 3:
    par = int(input('Quantas parcelas? '))
    final = price
    juros = final / par
    print(f'Sua compra será parcelada em {par}x de r${juros:.2F}.')
elif opc == 4:
    par = int(input('Quantas parcelas? '))
    final = price + price*20/100
    juros = final / par
    print(f'Sua compra será parcelada em {par}x de r${juros:.2F} COM JUROS.')
print(f'Sua compra de R${price:.2f} vai custar R${final:.2f} no final.')
