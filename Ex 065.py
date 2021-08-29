
soma=cont=maior=menor = 0
perg = 'sim'

while perg == 'sim':
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if maior<n:
            maior = n
        elif menor>n:
            menor = n
    perg = str(input('DESEJA CONTINUAR DIGITANDO OS VALORES [SIM/NÃO]:')).lower()

media = soma / cont
print('-'*30)
print('MEDIA = {:.1f}'.format(media))
print('-'*30)
print('MAIOR  = {}'.format(maior))
print('-'*30)
print('MENOR = {}'.format(menor))
print('-'*30)
