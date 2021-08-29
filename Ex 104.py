def leiaInt(numero):
    ok = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro digite um número válido!\033[m')
        if ok:
            break
    return valor
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
