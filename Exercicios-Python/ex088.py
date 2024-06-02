from random import randint
jogos = []
jogo = []
print('-'*50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-'*50)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
for c in range(1, quant+1):
    for d in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in jogo: 
                jogo.append(n)
                break
    jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {c}: {jogo}')
    jogo.clear()
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
