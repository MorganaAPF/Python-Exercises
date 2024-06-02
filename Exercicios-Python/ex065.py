opc = 'S'
cont = soma = maior = 0
while opc == 'S':
    num = int(input('Digite um número: '))
    opc = input('Quer continuar? [S/N] ').strip().upper()
    if cont == 0:
        menor = num
    elif num < menor:
        menor = num
    if num > maior:
        maior = num
    cont += 1
    soma += num
print(f'''Você digitou {cont} números e a média foi {soma/cont:.2f}
O maior valor foi {maior} e o menor foi {menor}''')
