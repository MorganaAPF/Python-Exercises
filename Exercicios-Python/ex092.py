from datetime import date
pessoa = {'Nome': input('Nome: '),
          'Idade': date.today().year - int(input('Ano de nascimento: ')),
          'CTPS': int(input('Carteira de trabalho (0 não tem): '))}
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Contratação'] - (date.today().year - pessoa['Idade']) + 35 
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
