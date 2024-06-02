"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade: até 9 anos = MIRIM; até 14 anos = INFANTIL; até 19 anos = JÚNIOR;
até 25 anos = SÊNIOR; acima de 25 anos = MASTER."""

from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    clas = 'MIRIM'
elif idade <= 14:
    clas = 'INFANTIL'
elif idade <= 19: 
    clas = 'JÚNIOR'
elif idade <= 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'
print(f'Classificação: {clas}')
