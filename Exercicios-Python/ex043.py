"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
seu status, de acordo com a tabela abaixo: – IMC abaixo de 18,5: Abaixo do Peso – Entre 18,5 e 25: Peso Ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade – Acima de 40: Obesidade Mórbida."""

peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / altura ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Essa pessoa está ABAIXO DO PESO normal.')
elif imc <= 25:
    print('PARABÉNS, essa é a faixa de PESO NORMAL.')
elif imc <= 30:
    print('Essa pessoa está em SOBREPESO.')
elif imc <= 40:
    print('Essa pessoa está em OBESIDADE!')
else:
    print('Essa pessoa está em OBESIDADE MÓRBIDA, cuidado!')
