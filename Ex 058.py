from random import randint
palpites = 0
comp = randint(0,10)
jogador = int(input('De 0 até 10,qual número o computador pensou? '))
while jogador != comp:
    palpites += 1
    print('Errou...')
    jogador = int(input('Digite novamente: '))
print('Acertou!!!')



