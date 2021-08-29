a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a>b:
    print('{} PRIMEIRO VALOR É MAIOR...'.format(a))
    print('{} SEGUNDO VALOR É MENOR...'.format(b))
elif b>a:
    print('{} PRIMEIRO VALOR É O MENOR...'.format(a))
    print('{} SEGUNDO VALOR É O MAIOR...'.format(b))
elif a==b:
    print('NÃO EXISTE VALOR MAIOR...')
    print('{} PRIMEIRO VALOR É IGUAL AO {} SEGUNDO VALOR...'.format(a,b))
