"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que
posição está o time do São Paulo."""

teams = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
         'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('-='*30)
print(f'Lista de times do Brasileirão: {teams}')
print('-='*30)
print(f'Os 5 primeiros colocados são {teams[:5]}')
print('-='*30)
print(f'Os 4 últimos são {teams[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(teams)})')
print('-='*30)
print(f'O São Paulo está na {teams.index('São Paulo')+1}ª posição.')
