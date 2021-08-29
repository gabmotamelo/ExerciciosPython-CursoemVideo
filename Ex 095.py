futebol = dict()
gols = list()
geral = list()
while True:
    futebol.clear()
    gols.clear()
    print('-' * 30)
    futebol['Nome']=str(input('Nome do Jogador:'))
    partidas = int(input(f'Quantas partidas {futebol["Nome"]} jogou? '))
    if partidas>0:
        for i in range(0,partidas):
            gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
    futebol['Gols']=gols[:]
    futebol['Total']=sum(gols)
    geral.append(futebol.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Digite S p/ sim ou N p/ não...')
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')
for i in futebol.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for i,j in enumerate(geral):
    print(f'{i:<3}',end='')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    dados = int(input('Mostrar dados de qual jogador?[* Digite "999" para encerrar!] '))
    if dados==999:
        break
    elif dados<=partidas:
        print(f'--- LEVANTAMENDO DO JOGADOR {geral[dados]["Nome"]}')
        for k,v in enumerate(geral[dados]["Gols"]):
            print(f'  No jogo {k+1} fez {v} gols.')
    elif dados>partidas:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente...')

