print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = cont = 0
opc = 10
while opc != 0:
    while c < opc:
        print(f'{pt} ->', end=' ')
        c += 1
        cont += 1
        pt += r
    print('PAUSA')
    c = 0
    opc = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados.')
