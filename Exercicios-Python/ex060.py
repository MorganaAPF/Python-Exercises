"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

f = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {f}! = {f}', end=' ')
r = f
c = f-1
while c > 0:
    print(f'x {c}', end=' ')
    r *= c
    c -= 1
print(f'= {r}')
