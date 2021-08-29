numeros = [[],[]]
for i in range(0,7):
    x=int(input(f'Digite o {i+1}º valor: '))
    if x%2==0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
numeros[0].sort()
numeros[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')

