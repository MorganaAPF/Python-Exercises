from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {hoje}.')
if idade < 18:
    quando = 18 - idade
    print(f"""Ainda faltam {quando} anos para o alistamento.
Seu alistamento será em {hoje + quando}.""")
elif idade > 18:
    quando = idade - 18
    print(f"""Você já deveria ter se alistado a {quando} anos.
Seu alistamento foi em {hoje - quando}.""")
else:
    print('Você tem que se alistar IMEDIATAMENTE!')  
