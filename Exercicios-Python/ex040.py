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
