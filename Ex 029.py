velocidade = int(input('Digite a velocidade do carro:'))
if velocidade>80:
    preco = (velocidade-80)*7.00
    print('Você atingiu {} km/h e foi multado!\nO preço da multa irá ser: R${:.2f} .'.format(velocidade ,preco))
print('Tenha um bom dia! Dirija com segurança!')
