"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m = l*a
print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {m}m².')
print(f'Para pintar essa parede, você precisará de {m/2}l de tinta.')
