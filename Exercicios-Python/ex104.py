"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""

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
