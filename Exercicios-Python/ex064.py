num = soma = cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont-1} números e a soma entre eles foi {soma}')
