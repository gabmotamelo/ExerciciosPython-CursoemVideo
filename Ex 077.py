palavras  = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
             'MERCADO','PROGRAMADOR','FUTURO')
for i in palavras:
    print(f'Palavra {i} temos ',end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra,end='')
    print('\n')