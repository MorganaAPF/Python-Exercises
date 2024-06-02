"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida, dizendo se ele foi aprovado (>=7), reprovado (<5), ou se está de recuperação (Entre 5 e 6.9)."""

a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
media = (a + b) / 2
print(f'Tirando {a} e {b}, a média do aluno é {media}')
if media >= 7:
    print('O aluno está APROVADO.')
elif media < 5:    
    print('O aluno está REPROVADO.')
else:
    print('O aluno está em RECUPERAÇÃO.')
