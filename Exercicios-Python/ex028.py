from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
pc = randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
print('PARABÉNS! Você conseguiu me vencer!' if n == pc else f'GANHEI! Eu pensei no número {pc} e não no {n}!')
