"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
de 1 até 500."""

count = soma = 0
for c in range(3, 501, 6):
        count += 1
        soma += c
print(f'A soma de todos os {count} valores é {soma}')
