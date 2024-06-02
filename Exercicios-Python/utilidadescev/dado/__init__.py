def leiaDinheiro(msg):
    while True:
        p = input(msg).strip().replace(',', '.')
        test = p.replace('.', '')
        if test.isnumeric():
            break
        print(f'ERRO! "{p}" é um preço inválido!')
    p = float(p)
    return p
