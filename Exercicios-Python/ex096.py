def area(l, a):
    print(f'A área de um terreno {l:.1f} x {a:.1f} é de {l*a:.1f}m²')


print('Controle de terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
a = float(input('ALTURA (m): '))
area(l, a)
