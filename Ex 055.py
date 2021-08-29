maior = 0
menor = 100
for i in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso>maior:
        maior = peso
        pessoamaior = i
    elif peso<menor:
        menor = peso
        pessoamenor = i

print('A {}ª PESSOA TEVE O MAIOR PESO({:.1f} KG)!\nA {}ª PESSOA TEVE O MENOR PESO({:.1f} KG)!'.format(pessoamaior,maior,pessoamenor,menor))
