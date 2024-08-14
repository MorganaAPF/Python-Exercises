def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Digite um número inteiro válido.')
        else:
            return n


def linha(tam = 42):
    print('-' * tam) 


def cabeçalho(txt):
    linha()
    print(f'{txt:^42}')
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for i, c in enumerate(lista):
        print(f'{i + 1} - {c}')
    linha()
    opc = leiaint('Sua opção: ')
    return opc
