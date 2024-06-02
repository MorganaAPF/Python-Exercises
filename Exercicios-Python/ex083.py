exp = input('Digite a expressão: ')
abre = fecha = 0
for c in exp:
    if c == '(':
        abre += 1
    elif c == ')':
        fecha += 1
    if fecha > abre:
        print('Sua expressão está errada!')
        break
if abre == fecha:
    print('Sua expressão está válida!')
