"""Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a
matriz na tela, com a formatação correta."""

matriz = [[], [], []]
for la in range(0, 3):
    for c in range(0, 3):
        matriz[la].append(int(input(f'Digite um valor para [{la}, {c}]: ')))
print('-='*50)
for c in matriz:
    for d in range(0, 3):
        print(f'[{c[d]:^5}]', end=' ')
    print('')
