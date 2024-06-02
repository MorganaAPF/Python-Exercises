"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

city = input('Em que cidade você nasceu? ').strip().capitalize()
print(city[:5] == 'Santo')
