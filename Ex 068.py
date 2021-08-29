from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vit = 0
while True:
    n = int(input('DIGA UM VALOR DE 0 ATÉ 10: '))
    while n not in range(0,11):
        n = int(input('DIGA UM VALOR DE 0 ATÉ 10: '))
    computador = randint(0,10)
    total = n + computador
    tipo = str(input('PAR OU ÍMPAR ? [P/I] ')).strip().upper()[0]
    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR ? [P/I] ')).strip().upper()[0]
    print('-'*30)
    print('Você jogou {} e o computador {}.Total de {} '.format(n, computador, total) ,end='')
    if total % 2 == 0:
        print('DEU PAR.')
        result = 'P'
    else:
        print('DEU ÍMPAR.')
        result = 'I'
    print('-'*30)
    if tipo == result:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-'*15)
        vit += 1
    else:
        print('Você PERDEU!')
        break
print('=-'*15)
if vit==1:
    print('GAME OVER! Você venceu {} vez.'.format(vit))
else:
    print('GAME OVER! Você venceu {} vezes.'.format(vit))