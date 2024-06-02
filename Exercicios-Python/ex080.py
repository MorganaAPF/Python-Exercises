"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

numbers = []
for a in range(0, 5):
    number = int(input('Digite um valor: '))
    if len(numbers) == 0 or number > numbers[-1]:
        numbers.append(number)
        print('Adicionado ao final da lista...')
    else:
        for b, c in enumerate(numbers):
            if number <= c:
                numbers.insert(b, number)
                print(f'Adicionado na posição {b} da lista...')
                break
print('-='*40)
print(f'Os valores digitados em ordem foram {numbers}')
