"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

n = float(input('Uma distância em metros: '))
print(f'A medida de {n}m corresponde a: ')
print(f'{n/1000}km')
print(f'{n/100}hm')
print(f'{n/10}dam')
print(f'{n*10:.0f}dm')
print(f'{n*100:.0f}cm')
print(f'{n*1000:.0f}mm')
