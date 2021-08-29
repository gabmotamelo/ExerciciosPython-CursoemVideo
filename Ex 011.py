largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura*altura
tinta = area/2
print('A área da parede é {:.2f}m² .\nE será necessário {:.3f} litros de tinta para pintar a parede.'.format(area,tinta))
