"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram
cadastrados. C) quantas mulheres tem menos de 20 anos."""

maiores = homens = m20 = 0
while True:
    print('-'*30)
    print(f'{"CADASTE UMA PESSOA":^30}')
    print('-'*30)
    idade = int(input('Idade : '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    if idade > 18:
        maiores += 1
    print('-'*30)
    yesno = input('Quer continuar? [S/N] ').strip().upper()
    if yesno == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maiores}
Ao todo temos {homens} homens cadastrados
E temos {m20} mulheres com menos de 20 anos''')
