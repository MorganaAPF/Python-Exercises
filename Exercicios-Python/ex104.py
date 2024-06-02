def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        else:
            print('ERRO! Digite um número válido.')
    return n


print('-' * 30)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
