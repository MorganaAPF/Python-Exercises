"""Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

from utilidadescev import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
