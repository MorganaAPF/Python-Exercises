"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere
que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
tot50 = tot20 = tot10 = tot1 = 0
value = int(input('Que valor você quer sacar? R$'))
while True:
    while value >= 50:
        value -= 50
        tot50 += 1
    if tot50 > 0:
        print(f'Total de {tot50} cédulas de R$50.00')
    while value >= 20:
        value -= 20
        tot20 += 1
    if tot20 > 0:
        print(f'Total de {tot20} cédulas de R$20.00')
    while value >= 10:
        value -= 10
        tot10 += 1
    if tot10 > 0:
        print(f'Total de {tot10} cédulas de R$10.00')
    while value >= 1:
        value -= 1
        tot1 += 1
    if tot1 > 0:
        print(f'Total de {tot1} cédulas de R$1.00')
    break
