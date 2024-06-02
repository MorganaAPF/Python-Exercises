"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele"""

v = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(v)}')
print(f'Só tem espaços? {v.isspace()}')
print(f'É um número? {v.isnumeric()}')
print(f'É alfabético? {v.isalpha()}')
print(f'É alfanumérico? {v.isalnum()}')
print(f'Está em maiúsculas? {v.isupper()}')
print(f'Está em minúsculas? {v.islower()}')
print(f'Está capitalizada? {v.istitle()}')
