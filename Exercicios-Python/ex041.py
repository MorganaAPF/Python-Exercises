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
