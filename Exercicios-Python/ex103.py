def ficha(nome='<desconhecido>', gols='0'):
    if nome == '' or nome.isspace():
        nome = '<desconhecido>'
    if gols == '' or gols.isspace() or gols.isnumeric() == False:
        gols = 0
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
ficha(nome, gols)
