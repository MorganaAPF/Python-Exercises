cont = velho = media = 0
for c in range(1, 5):
    print(f'{" {}ª PESSOA ":-^20}'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    media += idade
    sexo = input('Sexo [M/F]: ').strip().upper()
    if sexo == 'M' and idade > velho:
        velho = idade
        idoso = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f"""A média de idade do grupo é de {media / 4:.1f} anos.
O homem mais velho tem {velho} anos e se chama {idoso}.
Ao todo são {cont} mulheres com menos de 20 anos.""")
