def aumentar(num, quant, formata=False):
    num += num * quant / 100
    if formata == False:
        return num
    else:
        num = str(f'R${num:.2f}')
        num = num.replace('.', ',')
        return num


def diminuir(num, quant, formata=False):
    num -= num * quant / 100
    if formata == False:
        return num
    else:
        num = str(f'R${num:.2f}')
        num = num.replace('.', ',')
        return num


def dobro(num, formata=False):
    num *= 2
    if formata == False:
        return num
    else:
        num = str(f'R${num:.2f}')
        num = num.replace('.', ',')
        return num


def metade(num, formata=False):
    num /= 2
    if formata == False:
        return num
    else:
        num = str(f'R${num:.2f}')
        num = num.replace('.', ',')
        return num


def moeda(num):
    num = str(f'R${num:.2f}').replace('.', ',')
    return num


def resumo(p, plus, minus):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<28}', f'{moeda(p)}')
    print(f'{"Dobro do preço:":<28}', f'{dobro(p, True)}')
    print(f'{"Metade do preço:":<28}', f'{metade(p, True)}')
    print(f'{"{}% de aumento:":<28}'.format(plus), f'{aumentar(p, plus, True)}')
    print(f'{"{}% de redução:":<28}'.format(minus), f'{diminuir(p, minus, True)}')
