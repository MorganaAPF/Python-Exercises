numbers = []
yesno = 'S'
while yesno != 'N':
    numbers.append(int(input('Digite um valor: ')))
    yesno = input('Quer continuar? [S/N] ').strip().upper()
numbers.sort(reverse=True)
print('-='*50)
print(f'''Você digitou {len(numbers)} elementos.
Os valores em ordem decrescente são {numbers}''')
print('O valor 5 faz parte da lista!') if 5 in numbers else print('O valor 5 não foi encontrado na lista!')
