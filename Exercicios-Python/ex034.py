sal = float(input("Qual é o salário do funcionário? R$"))
if sal > 1250:
    aumento = sal*10/100 + sal 
else:
    aumento = sal*15/100 + sal
print(f'Quem ganhava R${sal:.2f} passa a ganhar {aumento:.2f} agora.')
