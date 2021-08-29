futebol = dict()
gols = list()
futebol['Nome']=str(input('Nome do Jogador:'))
partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
if partidas>0:
    for i in range(0,partidas):
        gols.append(int(input(f"Quantos gols na partida {i}? ")))

futebol['Gols']=gols[:]
futebol['Total']=sum(gols)
print('-='*30)
print(futebol)
print('-='*30)
for k,v in futebol.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
if partidas==1:
    print(f'O jogador {futebol["Nome"]} jogou {partidas} partida.')
else:
    print(f'O jogador {futebol["Nome"]} jogou {partidas} partidas.')
for i in range(0,partidas):
    if gols[i]==1:
        print(f'=> Na partida {i},fez {gols[i]} gol.')
    else:
        print(f'=> Na partida {i},fez {gols[i]} gols.')
if futebol["Total"]==1:
    print(f'Foi um total de {futebol["Total"]} gol.')
else:
    print(f'Foi um total de {futebol["Total"]} gols.')


