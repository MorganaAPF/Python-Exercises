from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Qauarto aluno: ')
lista = [a1, a2, a3, a4]
print(f'O aluno escolhido foi: {choice(lista)}')
