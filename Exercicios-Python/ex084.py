"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

lista = []
temp = []
yesno = 'S'
while yesno != 'N':
    temp.append(input('Nome: '))
    peso = float((input('Peso: ')))
    temp.append(peso)
    if len(lista) == 0:
        menor = maior = peso
    elif peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
    lista.append(temp[:])
    temp.clear()
    yesno = input('Quer continuar? [S/N] ').strip().upper()
print('-='*30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de', end=' ')
for c in lista:
    if c[1] == maior:
        print(c[0], end=' ')
print(f'\nO menor peso doi de {menor:.1f}Kg. Peso de', end=' ')
for c in lista:
    if c[1] == menor:
        print(c[0], end=' ')
