from random import randint
from time import sleep
lista = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

perguntar = int(input('''Escolha uma opção para jogar:
[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha [0/1/2] = '''))
print('JO\n')
sleep(1)
print('KÊN\n')
sleep(1)
print('PÔ')
sleep(1)
print(10*'-=-')
if perguntar==0:
    print('O jogador escolheu PEDRA!')
elif perguntar==1:
    print('O jogador escolheu PAPEL!')
elif perguntar==2:
    print('O jogador escolheu TESOURA!')
print(10*'-=-')
if computador==0:
    print('O computador escolheu PEDRA!')
elif computador==1:
    print('O computador escolheu PAPEL!')
elif computador==2:
    print('O computador escolheu TESOURA!')
print(10*'-=-')

if perguntar==0 and computador==0:
    print('EMPATE!')
elif perguntar==0 and computador==1:
    print('COMPUTADOR VENCEU!')
elif perguntar==0 and computador==2:
    print('VOCÊ VENCEU!')
elif perguntar==1 and computador==0:
    print('VOCÊ VENCEU!')
elif perguntar==1 and computador==1:
    print('EMPATE!')
elif perguntar==1 and computador==2:
    print('COMPUTADOR VENCEU!')
elif perguntar==2 and computador==0:
    print('COMPUTADOR VENCEU!')
elif perguntar==2 and computador==1:
    print('JOGADOR VENCEU!')
elif perguntar==2 and computador==2:
    print('EMPATE!')

