numeros = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        print('=-' * 30)
        break

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')