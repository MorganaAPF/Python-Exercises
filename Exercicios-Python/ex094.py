lista = []
yesno = 'p'
m = 0
while yesno != 'N':
    yesno = 'p'
    pessoa = {'Nome': input('Nome: '), 'Sexo': 'd'}
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['Sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa)
    while yesno not in 'SN':
        yesno = input('Quer continuar? [S/N] ').strip().upper()
        if yesno not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')            
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for c in lista:
    m += c['Idade']
m /= len(lista)
print(f'B) A média de idade é de {m:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for c in lista:
    if c['Sexo'] == 'F':
        print(c['Nome'], end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for c in lista:
    if c['Idade'] > m:
        print(f'    {c['Nome']} com {c['Idade']} anos.')
print('<< ENCERRADO >>')
