"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

alunos = []
yesno = 'S'
while yesno != 'N':
    nome = input('Nome: ').strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], m])
    yesno = input('Quer continuar? [S/N] ').strip().upper()
print('-='*35)
print('No. NOME', end='')
print(f'{"MÉDIA":>13}')
print('-'*24)
for i, c in enumerate(alunos):
    print(f'{i}   {c[0]:<13}', end='')
    print(f'{c[2]:.1f}')
while True:
    print('-'*24)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('''FINALIZANDO...
<<< VOLTE SEMPRE >>>''')
