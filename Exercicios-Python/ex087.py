matriz = [[], [], []]
ter = pares = maior = 0
for la in range(0, 3):
    for c in range(0, 3):
        n = (int(input(f'Digite um valor para [{la}, {c}]: ')))
        matriz[la].append(n)
        if n % 2 == 0:
            pares += n
        if c == 2:
            ter += n
        if la == 1:
            if n > maior:
                maior = n 
print('-='*50)
for c in matriz:
    for d in c:
        print(f'[{d:^5}]', end=' ')
    print('')
print('-='*50)
print(f'''A soma dos valores pares é {pares}.
A soma dos valores da terceira coluna é {ter}.
O maior valor da segunda linha é {maior}.''')
