v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print(f"""MULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${(v - 80)*7:.2f}!""")
print('Tenha um bom dia! Dirija com segurança!')
