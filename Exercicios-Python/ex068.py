from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
w = 0
while True:
    p = int(input('Digite um valor: '))
    pc = randint(1, 10)
    pi = input('Par ou ímpar? [P/I] ').strip().upper()
    print('-'*40)
    if p + pc % 2 == 0:
        game = 'PAR'
        r = 'P'
    else:
        game = 'ÍMPAR'
        r = 'I'
    print(f'Você jogou {p} e o computador jogou {pc}. Total de {p+pc} DEU {game}')
    print('-'*40)
    if pi == r:
        print('''VOCÊ VENCEU!
Vamos jogar novamente...''')
        w += 1
    else:
        print('VOCÊ PERDEU!')
        break
    print('-='*20)
print('-='*20)
print(f'GAME OVER! Você venceu {w} vezes.')
