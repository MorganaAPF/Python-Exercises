"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

n = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${n:.2f}, na promoção com desconto de 5% vai custar R${n-n*5/100:.2f}')
