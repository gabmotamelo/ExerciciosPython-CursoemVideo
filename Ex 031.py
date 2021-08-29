distancia = float(input('Digite a distância da viagem KM : '))
if distancia<=200:
    preco = 0.50 * distancia
    print('O preço da passagem irá ser de : R${:.2f}'.format(preco))
else:
    preco  = 0.45 * distancia
    print('O preco da passagem irá ser de : R$ {:.2f}'.format(preco))
