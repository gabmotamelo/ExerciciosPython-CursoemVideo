num = list()
while True:
    aux = int(input('Digite um valor: '))
    if aux not in num:
        num.append(aux)
    else:
        print('Valor duplicado! Não vou adicionar...')
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        print(sorted(num))
        print('=-'*30)
        break
