nome = input('Digite seu nome completo: ').strip()
split = nome.split()
print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(' ', ''))} letras')
print(f'Seu primeiro nome é {split[0].capitalize()} e ele tem {len(split[0])} letras')
