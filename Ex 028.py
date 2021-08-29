from random import randint
num = (randint(0,5))
usuario = int(input('De 0 até 5,qual número o computador pensou? '))
if usuario == num:
    print('Você acertou!')
else:
    print('Você errou!')
    print('O número era : {}! '.format(num))
