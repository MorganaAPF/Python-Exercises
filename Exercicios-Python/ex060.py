f = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {f}! = {f}', end=' ')
r = f
c = f-1
while c > 0:
    print(f'x {c}', end=' ')
    r *= c
    c -= 1
print(f'= {r}')
