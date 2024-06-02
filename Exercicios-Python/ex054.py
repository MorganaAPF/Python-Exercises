"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores."""

from datetime import date

maiores = menores = 0
for c in range(1, 8):
    a = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if date.today().year - a < 21:
        menores += 1
    else:
        maiores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade e {menores} pessoas menores de idade.')
