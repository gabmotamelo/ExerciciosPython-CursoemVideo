salario = float(input('Digite o salário: '))
if salario>1250:
    novosalario=(salario*0.10)+salario
else:
    novosalario=(salario*0.15)+ salario
print('Você ganhava R${:.2f},teve um aumento e irá ganhar R${:.2f}'.format(salario, novosalario))