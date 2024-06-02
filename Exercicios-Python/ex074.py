from random import randint
numbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
sort = sorted(numbers)
print(f'Os valores sorteados foram:', end=' ')
for c in numbers:
    print(f'{c}', end=' ')
print(f'''\nO maior valor sorteado foi {sort[-1]}
O menor valor sorteado foi {sort[0]}''')
