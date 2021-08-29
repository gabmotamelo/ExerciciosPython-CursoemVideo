import math
angulo = int(input('Digite o valor do ângulo: '))
tan = math.tan(math.radians(angulo))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
print('O ângulo é {}º.\nO valor do SENO é {:.2f}.\nO valor do COSSENO é {:.2f}.'
      '\nO valor da TANGENTE é {:.2f}.'.format(angulo , sen , cos , tan))
