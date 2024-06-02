cont1 = ''
frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
print(f'O inverso de {frase} é', end=' ')
for c in range(len(frase) - 1, -1, -1):
    cont1 += frase[c]
    print(frase[c], end='')
if cont1 == frase:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase digitada não é um palíndromo!')
