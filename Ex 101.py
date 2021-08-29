def voto(n=0):
    idade = 2021-n
    if idade<16:
        return 'Voto Negado!'
    elif idade>=18 and idade<70:
        return 'Voto Obrigatório!'
    else:
        return 'Voto Opcional!'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))


