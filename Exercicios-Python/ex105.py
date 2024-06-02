"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
A) Quantidade de notas
B) A maior nota
C) A menor nota
D) A média da turma
E) A situação (opcional)"""

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    todas = {'Total': len(num), 'Maior': max(num), 'Menor': min(num), 'Média': float(f'{sum(num) / len(num):.2f}')}
    if sit:
        if todas['Média'] < 5:
            todas['Situação'] = 'RUIM'
        elif todas['Média'] < 7:
            todas['Situação'] = 'RAZOÁVEL'
        else:
            todas['Situação'] = 'BOA'
    return todas


resp = (notas(5.5, 2.5, 1.5, sit=True))
print(resp)
help(notas)
