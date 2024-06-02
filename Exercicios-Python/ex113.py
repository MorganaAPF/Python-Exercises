def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro válido.')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('ERRO! Digite um número real válido.')
        else:
            return n


print('-' * 30)
n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
