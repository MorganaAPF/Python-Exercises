"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador = {'Nome': input('Nome do jogador: '), 'Gols': []}
for c in range(0, int(input(f'Quantas partidas {jogador['Nome']} jogou? '))):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
print('-=' * 40)
jogador['Total'] = sum(jogador['Gols'])
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.')
for i, c in enumerate(jogador['Gols']):
    print(f'=> Na partida {i+1}, fez {c} gols')
print(f'Foi um total de {jogador['Total']} gols.')
