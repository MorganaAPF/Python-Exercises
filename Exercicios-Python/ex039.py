"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo."""

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
