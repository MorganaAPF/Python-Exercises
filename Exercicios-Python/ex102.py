def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    print('-' * 30)
    fact = num
    if show:
        print(num, end=' ')
    for c in range(num - 1, 0, -1):
        if show:
            print(f'x {c}', end=' ')
        fact *= c
    if show:
        print(f'=', end=' ')
    return fact


help(fatorial)
print(fatorial(5, show=True))
