"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior."""

from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        num.append(randint(1, 10))
        sleep(0.3)
        print(num[c], end=' ', flush=True)
    print('PRONTO!')


def somapar(num):
    s = 0
    for c in num:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {num}, temos {s}')


numeros = []
sorteia(numeros)
somapar(numeros)
