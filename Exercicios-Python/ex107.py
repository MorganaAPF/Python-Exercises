"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

from utilidadescev import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10)}')
