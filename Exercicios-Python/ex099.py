from time import sleep


def maiores(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in num:
        sleep(0.2)
        print(c, end=' ', flush=True)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}')
    else:
        print(f'O maior valor informado foi 0')
    

maiores(2, 9, 4, 5, 7, 1)
maiores(4, 7, 0)
maiores(1, 2)
maiores(6)
maiores()
