"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
programa tem que realizar três contagens através da função criada:
A) de 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) uma contagem personalizada"""

from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} contando de {p} em {p}')
    sleep(1)
    if f < i: 
        f -= 1
        if p > 0:
            p *= -1
    else:
        f += 1
    if p == 0:
        p = 1
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.2)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
