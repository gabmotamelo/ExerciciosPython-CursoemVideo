times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí')
print()
print('Lista de times do Brasileirão: {}'.format(times))
print()
print('Os 5 primeiros são: {}'.format(times[0:5]))
print()
print('Os 4 últimos são: {}'.format(times[-4:]))
print()
print('Times em ordem alfabética: {}'.format(sorted(times)))
print()
print('A Chapecoense está na {}ª posição'.format(times.index('Chapecoense')+1))