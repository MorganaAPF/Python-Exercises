"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no
dado."""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogardor1': randint(1, 6), 'jogardor2': randint(1, 6),
        'jogardor3': randint(1, 6), 'jogardor4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*40)
print('== RANKING DOS JOGADORES ==')
for k, v, in enumerate(ranking):
    sleep(0.5)
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
