print('='*30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('='*30)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
s = n
for c in range(0, 10):
    print(f'{s} ->', end=' ')
    s += r
print('ACABOU')
