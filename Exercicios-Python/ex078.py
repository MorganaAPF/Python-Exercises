numbers = []
for c in range(0, 5):
    numbers.append(int(input(f'Digite um valor para a posição {c}: ')))
sortedd = sorted(numbers)
higher = sortedd[-1]
lower = sortedd[0]
print('=-'*50)
print(f'Você digitou os valores {numbers}')
print(f'O maior valor digitado foi {higher} nas posições', end=' ')
for v, c in enumerate(numbers):
    if c == higher:
        print(f'{v}...', end=' ')
print(f'\nO menor valor digitado foi {lower} nas posições', end=' ')
for v, c in enumerate(numbers):
    if c == lower:
        print(f'{v}...', end=' ')
