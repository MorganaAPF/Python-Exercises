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
