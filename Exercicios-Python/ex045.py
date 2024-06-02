"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

pc = randint(0, 2)
if pc == 0:
    pct = 'Pedra'
elif pc == 1:
    pct = 'Papel'
else:
    pct = 'Tesoura'
p = int(input("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? """))
if p == 0:
    pt = 'Pedra'
elif p == 1:
    pt = 'Papel'
else:
    pt = 'Tesoura'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 15)
print(f"""Computador jogou {pct}
Jogador jogou {pt}""")
print('-=' * 15)
if p == 0 and pc == 2 or p == 1 and pc == 0 or p == 2 and pc == 1:
    print('JOGADOR VENCE!')
elif pc == 0 and p == 2 or pc == 1 and p == 0 or pc == 2 and p == 1:
    print('COMPUTADOR VENCE!')
else:
    print('EMPATE!')
