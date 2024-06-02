"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem dizendo qual é o
maior ou se são iguais."""

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O PRIMEIRO valor é maior.')
elif b > a:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')
