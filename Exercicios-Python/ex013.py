"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

n = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${n:.2f}, com 15% de aumento, passa a receber R${n+n*15/100:.2f}')
