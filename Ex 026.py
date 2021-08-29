frase = str(input('Digite uma frase:')).lower()
print('Quantas vezes aparece a letra "A" : {}'.format(frase.count('a')))
print('Qual posição aparece a letra "A" pela primeira vez : {}'.format(frase.find('a')+1))
print('Qual á ultima posição que aparece a letra "a" : {} '.format(frase.rfind('a')+1))

