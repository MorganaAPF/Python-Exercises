print('-'*40)
print('Sequência de Fibonacci')
print('-'*40)
termos = int(input('Quantos termos você quer mostrar? '))
c = t1 = 0
t2 = 1
print('~'*40)
while c < termos:
    print(f'{t1} -> {t2}', end=' -> ')
    t1 = t1 + t2
    t2 = t1 + t2  
    c += 2
print('FIM')
print('~'*40)
