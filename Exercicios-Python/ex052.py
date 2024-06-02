"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

div = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        div += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {div} vezes')
if div > 2 or div == 1:
    print('e por isso ele NÃO É PRIMO!')
else:
    print('e por isso ele É PRIMO!')
