from time import sleep
def contador(x,y,z):
    print('-='*20)
    print(f'Contagem de {x} até {y} passo {z}')
    print('-=' * 20)
    for i in range(x,y,z):
        print(i,end=' ')
        sleep(0.5)
    print('FIM!')
    print()
contador(1,11,1)
contador(10,0,-2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
if x<0:
    z *= -1
print('-=' * 20)
contador(x,y,z)




