menor = 0
maior = 0
for i in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa : '.format(i)))
    idade = 2021 - ano
    if idade>18:
        maior += 1
    else:
        menor += 1

print('MAIORES DE IDADE: {}\nMENORES DE IDADE: {}'.format(maior,menor))
