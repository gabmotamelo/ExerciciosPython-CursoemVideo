numeros = list()
total = 0
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        total += 1
    else:
        print('Valor duplicado! Não vou adicionar...')
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if decisao=='N':
        print('=-' * 30)
        break
print(f'Você digitou {total} elementos. ')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista!')
