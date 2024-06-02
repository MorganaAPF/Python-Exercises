numbers = []
yesno = 'S'
while yesno != 'N':
    number = input('Digite um valor: ')
    while not number.isnumeric():
        number = input('Por favor, digite um valor válido! ')
    if number in numbers:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        numbers.append(number)
        yesno = input('Quer continuar? [S/N] ').strip().upper()
    while yesno not in 'SN':
        yesno = input('Resposta inválida! Por favor, digite "S" para sim ou "N" para não: ').strip().upper()
print('-='*40)
print(f'Você digitou os valores {sorted(numbers)}')
