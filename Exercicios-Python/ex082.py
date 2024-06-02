"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

full = []
even = []
odd = []
yesno = 'S'
while yesno != 'N':
    num = int(input('Digite um número: '))
    full.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    yesno = input('Quer continuar? [S/N] ').strip().upper()
print('-='*50)
print(f'''A lista de completa é {full}
A listas de pares é {even}
A lista de ímpares é {odd}''')
