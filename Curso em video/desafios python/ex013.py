salario = float(input('Qual é  osalario do Funcionario? R$'))
novosalario = salario + (salario * 15 / 100)
print('Um Funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novosalario))