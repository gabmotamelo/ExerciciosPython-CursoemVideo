def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip()=='':
    ficha(gol=gols)
else:
    ficha(nome,gols)

