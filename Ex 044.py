preco = float(input('Digite o preço do produto: '))
forma = str(input('Digite a forma de pagamento(DINHEIRO/CHEQUE/CARTÃO):')).lower()
if forma=='dinheiro' or forma=='cheque':
    precodesconto = preco-(0.10*preco)
    print('TOTAL = R${:.2f}\nVALOR FINAL A SER PAGO COM 10% DE DESCONTO = R${:.2f}'.format(preco,precodesconto))
elif forma=='cartão' or forma=='cartao':
    condição = str(input('Digite a condição de pagamento no cartão(Á VISTA/PARCELADO):')).lower()
    if condição=='á vista' or condição=='a vista':
        valor = preco-(preco*0.05)
        print('TOTAL = R${:.2f}\nVALOR FINAL A SER PAGO Á VISTA COM 5% DE DESCONTO = R${:.2f}'.format(preco,valor))
    elif condição=='parcelado':
        vezes = int(input('Quantas vezes vai ser parcelado: '))
        if vezes==2:
            parcela = preco/2
            print('TOTAL = R${:.2f}\nSerá parcelado em 2x de R${:.2f} '.format(preco,parcela))
        elif vezes>=3:
            total = preco+(preco*0.20)
            preco = total/vezes
            print('TOTAL COM JUROS DE 20% = R${:.2f}\nSerá parcelado em {}x de R${:.2f}'.format(total,vezes,preco))


