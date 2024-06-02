"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

pc = randint(0, 10)
p = int(input("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é seu palpite? """))
c = 1
while p != pc:
    if p > pc:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez')
    p = int(input('Qual é seu palpite? '))
    c += 1
print(f'Acertou com {c} tentativas. Parabéns!')
