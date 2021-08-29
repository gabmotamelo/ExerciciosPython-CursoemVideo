from random import randint
def sorteia(lista):
    print(f'Sorteando cinco valores da lista : ',end='')
    for i in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor%2==0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numero = list()
sorteia(numero)
somaPar(numero)
