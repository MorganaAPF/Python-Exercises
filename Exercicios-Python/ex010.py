"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

n = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${n:.2f} você pode comprar U${n*0.20:.2f}')
