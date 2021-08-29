cont = soma = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n==999:
        break
    soma += n
    cont += 1
print('SOMA DOS NÚMERO = {}'.format(soma))
print('FORAM DIGITADOS = {}'.format(cont))
