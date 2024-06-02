"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO
(todos os lados iguais), ISCÓCELES (dois lados iguais e um diferente), ESCALENO (todos os lados diferentes)."""

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        tipo = 'EQUILÁTERO'
    elif a != b and a != c and b != c:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓCELES'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo}!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
