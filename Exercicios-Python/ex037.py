"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

n = int(input('Digite um número inteiro: '))
opc = int(input("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """))
if opc == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opc == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opc == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
