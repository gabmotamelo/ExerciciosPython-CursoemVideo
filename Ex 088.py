print('-'*35)
print(f'{"JOGO DA MEGA SENA":^35} ')
print('-'*35)
from random import sample
quant = int(input('Quantos jogos? '))
for i in range(1, quant+1):
    jogo = [sample(range(1, 60), 6)]
    print(f'Jogo {i}: {jogo}')
    jogo.clear()