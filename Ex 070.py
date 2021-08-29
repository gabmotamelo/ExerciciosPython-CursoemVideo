print('='*30)
print('        LOJA SUPER BARATÃO')
print('='*30)
total = maiores = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: ')).upper()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco>1000:
        maiores += 1
    if cont==1:
        barato = nome
        precobarato = preco
    else:
        if preco<precobarato:
            barato = nome
            precobarato = preco
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('========== FIM DO PROGRAMA ==========')
print()
print('O total da compra foi R${:.2f}'.format(total))
if maiores==1:
    print('Temos {} produto custando mais de R$1000.00 '.format(maiores))
else:
    print('Temos {} produtos custando mais que R$1000.00'.format(maiores))
print('O produto mais barato foi {} que custa R${:.2f}'.format(barato,precobarato))
