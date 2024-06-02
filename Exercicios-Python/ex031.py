d = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d}Km.')
print('E o preço da sua passagem será de ', end='R$')
print(f'{d*0.50:.2f}' if d <= 200 else f'{d*0.45:.2f}')
