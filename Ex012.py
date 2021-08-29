preco = float(input('Digite o preço do produto:'))
desconto = preco - (preco*0.05)
print('O preço do produto é R${} .\nO produto com 5% de desconto é R${:.2f} .'.format(preco , desconto))
