"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if 17 < idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('-' * 30)
voto = voto(int(input('Em que ano você nasceu? ')))
print(voto)
