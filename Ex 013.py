salario = float(input('Digite o salário atual: '))
novo = (salario*0.15)+salario
print('O salário é R${} .\nO salário atualizado com 15% de aumento é R${:.2f} .'.format(salario , novo))
