matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for x in range(0,3):
        matriz[i][x]=int(input(f'Digite um valor para [{i},{x}]: '))
print('=-'*30)
for i in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[i][x]}]',end='')
    print()
print('=-'*30)


