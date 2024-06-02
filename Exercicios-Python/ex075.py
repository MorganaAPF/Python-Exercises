"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas
vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares."""

cont = 0
numbers = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'''Você digitou os valores {numbers}
O valor 9 apareceu {numbers.count(9)} vezes''')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for cc in numbers:
    if cc % 2 == 0:
        cont += 1
if cont > 0:
    print('Os valores pares digitados foram', end=' ')
    for c in numbers:
        if c % 2 == 0:
            print(c, end=' ')
else:
    print('Nenhum número par foi digitado')
