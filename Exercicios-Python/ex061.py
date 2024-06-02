print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(f'{pt} ->', end=' ')
    c += 1
    pt += r
print('FIM')
