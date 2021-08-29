from math import hypot
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
print('O cateto oposto é {}.\nO cateto adjacente é {}.\n'
      'A hipotenusa vai medir {:.2f}.'.format(oposto , adjacente , hypot(oposto,adjacente)))
