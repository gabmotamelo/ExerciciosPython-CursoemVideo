n = int(input('Digite um número inteiro:'))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro:'))
print('-'*30)
print('SOMA NÚMEROS DIGITADOS : {}'.format(soma))
print('-'*30)
print('QUANTIDADE DE NÚMEROS : {}'.format(cont))
print('-'*30)
print('FIM!!!')
