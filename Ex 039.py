ano = int(input('Digite o ano de nascimento: '))
idade = 2021-ano
if idade<18:
    tempo=18-idade
    print('Você ainda vai se alistar!')
    if tempo>1:
        print('Falta {} anos para se alistar...'.format(tempo))
    else:
        print('Falta {} ano para se alistar...'.format(tempo))
elif idade == 18:
    print('Já está na idade de se alistar!')
elif idade>18:
    tempo=idade-18
    print('Você passou do prazo de se alistar!')
    if tempo>1:
        print('Passou {} anos do seu prazo de alistamento...'.format(tempo))
    else:
        print('Passou {} ano do seu prazo de alistamento...'.format(tempo))