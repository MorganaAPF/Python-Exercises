a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    opc = int(input("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
> Qual é a sua opção? """))
    if opc == 1:
        print(f'O resultado de {a} + {b} é {a+b}.')
    elif opc == 2:
        print(f'O resultado de {a} x {b} é {a*b}.')
    elif opc == 3:
        if a > b:
            maior = a
        elif b > a:
            maior = b
        if a == b:
            print('Os dois números são iguais!')
        else:
            print(f'Entre {a} e {b} o maior é {maior}.')
    elif opc == 4:
        a = int(input("""Informe os números novamente:
Primeiro valor: """))
        b = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*15)
print('Fim do programa! Volte sempre!')
