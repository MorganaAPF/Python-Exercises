time = []
while True:
    jogador = {'Nome': input('Nome do jogador: '), 'Gols': []}
    for c in range(0, int(input(f'Quantas partidas {jogador['Nome']} jogou? '))):
        jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Total'] = sum(jogador['Gols'])
    time.append(jogador)
    yesno = input('Quer continuar? [S/N]: ').strip().upper()
    if yesno == 'N':
        break
print('-=' * 40)
print(f'cod nome{'gols':>15}{'total':>15}')
print('-'*39)
for i, c in enumerate(time):
    print(f'{i:>3} {c['Nome']:<15}{str(c['Gols']):<15}{c['Total']}')
while True:
    print('-' * 39)
    yn = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if yn == 999:
        break
    if yn > len(time) - 1:
        print(f'ERRO! Não existe jogador com o código {yn}!')
        continue
    print(f'-- LEVANTAMENTO DO JOGADOR {time[yn]['Nome']}')
    for i, c in enumerate(time[yn]['Gols']):
        print(f'No jogo {i+1} fez {c} gols.')
print('<< VOLTE SEMPRE >>')
