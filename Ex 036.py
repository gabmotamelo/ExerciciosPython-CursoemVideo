valor = float(input('Qual o valor da casa : '))
salario = float(input('Qual o salario do comprador: '))
anos = float(input('Em quantos anos irá pagar: '))
preco = valor/(anos*12)
limite = 0.30*salario

if preco<=limite:
    print('Empréstimo aprovado,terá uma parcela mensal de R${:.2f}'.format(preco))
elif preco>limite:
    print('Empréstimo negado,a parcela excedeu o limite de 30% do salário.')

