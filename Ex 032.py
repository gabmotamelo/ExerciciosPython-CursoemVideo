ano = int(input('Digite o ano: '))
dezena = ano%100
if dezena%4==0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')


