maior = homens = mulheres = 0
while True:
    print('='*30)
    print('CADASTRE UMA PESSOA')
    print('='*30)
    idade = int(input('Idade: '))
    while idade not in range(0,119):
        idade = int(input('Idade: '))
    if idade>18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo=='M':
        homens += 1
    elif sexo=='F':
        if idade<20:
            mulheres += 1
    print('='*30)
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while decisao not in 'SN':
        decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if decisao=='N':
        break
print('====== FIM DO PROGRAMA ======')
print()
print('Total de pessoas com mais de 18 anos: {}'.format(maior))
if homens==1:
    print('Ao todo temos {} homem cadastrado'.format(homens))
else:
    print('Ao todo temos {} homens cadastrados'.format(homens))
if mulheres==1:
    print('E temos {} mulher cadastrada com menos de 20 anos.'.format(mulheres))
else:
    print('E temos {} mulheres cadastradas com menos de 20 anos.'.format(mulheres))
