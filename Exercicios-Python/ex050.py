soma = pares = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares += 1
        soma += n
print(f'Você informou {pares} números pares e o resultado da soma deles foi de {soma}.')
