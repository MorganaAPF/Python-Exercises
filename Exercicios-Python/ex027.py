nome = input('Digite seu nome completo:  ').strip()
split = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {split[0]}')
print(f'Seu último nome é {split[len(split) - 1]}')
