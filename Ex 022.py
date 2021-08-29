nome = input('Digite o nome de uma pessoa:')
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras tem o nome: {}'.format( len(nome) - nome.count(' ')))
espaco = nome.split()
print('O primeiro nome tem {} letras.'.format(len(espaco[0])))

