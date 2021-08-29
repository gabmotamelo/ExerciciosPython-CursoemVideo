matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for x in range(0,3):
        matriz[i][x]=int(input(f'Digite um valor para [{i},{x}]: '))
print('=-'*30)
for i in range(0,3):
    for x in range(0,3):
        print(f'[ {matriz[i][x]} ]',end='')
    print()
print('=-'*30)
pares = terceira = maior = 0
for i in range(0,3):
    for x in range(0,3):
        if matriz[i][x]%2==0:
            pares += matriz[i][x]
for i in range(0, 3):
    for x in range(0, 3):
        if matriz[i]==matriz[x]:
            terceira += matriz[i][x]
for i in range(0,3):
    if matriz[1][i]>maior:
        maior = matriz[1][i]
print(f'A soma dos valores pares é {pares}')
print(f'A soma da terceira coluna {terceira}')
print(f'O maior valor da segunda linha é {maior}')
