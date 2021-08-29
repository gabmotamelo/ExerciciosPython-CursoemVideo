frase = str(input('Difite uma frase: '))
frasesemespaco = frase.replace(' ','')
frasenova = frasesemespaco.lower()
frasefinal=frasenova[::-1]
if frasefinal==frasesemespaco:
    print(frase)
    print('É UM PALINDROMO!')
else:
    print(frase)
    print('NÃO É UM PALÍNDROMO!')

