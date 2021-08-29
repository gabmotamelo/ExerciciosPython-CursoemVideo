total = 0
velho = 0
genero = 0
for i in range(1,5):
    nome = str(input('Digite o NOME da {}ª pessoa :'.format(i)))
    idade = int(input('Digite a IDADE da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o SEXO da {}ª pessoa [M/F]:'.format(i))).lower()
    total += idade
    if sexo=='m' and idade>velho:
        velho = idade
        nomevelho = nome
    elif sexo=='f' and idade<20:
        genero += 1
media = total/4
print()
print('A MÉDIA DE IDADE DO GRUPO É: {} anos'.format(media))
print('{} É O HOMEM MAIS VELHO!'.format(nomevelho.upper()))
print('QUANTIDADE DE MULHERES MENORES DE 20 ANOS: {}'.format(genero))
