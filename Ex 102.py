def fatorial(num,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show:(opcional) Mostrar ou não a conta(passo-a-passo)
    :return:O valor do Fatorial de um número 'num'.
    """
    fat = 1
    for i in range(num,0,-1):
        if show:
            print(i, end='')
            if i>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        fat *= i
    return fat


#print(fatorial(6,show=True))
help(fatorial)