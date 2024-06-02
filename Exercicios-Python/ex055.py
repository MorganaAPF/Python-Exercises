for c in range(1, 6):
    a = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        menor = a
        maior = a
    elif a > maior:
        maior = a
    elif a < menor:
        menor = a
print(f'O maior peso lido foi {maior:.1f}Kg')
print(f'O menor peso lido foi {menor:.1f}Kg')
