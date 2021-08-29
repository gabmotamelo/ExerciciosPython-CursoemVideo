x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
menu = int(input('''O QUE DESEJA FAZER:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

DIGITE A OPÇÃO DESEJADA:'''))
while menu != 5:
    if menu==1:
        soma = x+y
        print('SOMA DE {} + {} = {}'.format(x,y,soma))
        print()
        menu = int(input('''O QUE DESEJA FAZER:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa

        DIGITE A OPÇÃO DESEJADA:'''))
    elif menu==2:
        multiplicar = x*y
        print('MULTIPLICAÇÃO DE {} X {} = {} '.format(x,y,multiplicar))
        print()
        menu = int(input('''O QUE DESEJA FAZER:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa

        DIGITE A OPÇÃO DESEJADA:'''))
    elif menu==3:
        if x>y:
            print('MAIOR = {}'.format(x))
            print()
            menu = int(input('''O QUE DESEJA FAZER:
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa

            DIGITE A OPÇÃO DESEJADA:'''))
        else:
            print('MAIOR = {}'.format(y))
            print()
            menu = int(input('''O QUE DESEJA FAZER:
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa

            DIGITE A OPÇÃO DESEJADA:'''))
    elif menu==4:
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        print()
        menu = int(input('''O QUE DESEJA FAZER:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa

        DIGITE A OPÇÃO DESEJADA:'''))
        print()
from time import sleep
print('SAINDO DO PROGRAMA...')
sleep(1)
print('SAINDO...')
sleep(1)
print('SAÍDA EXECUTADA COM SUCESSO!!!')