from time import sleep
while True:
    print('-'*30)
    n = int(input('TABUADA DE QUAL NÚMERO = '))
    print('-'*30)
    if n <0:
        break
    for i in range(1,11):
        print('{} X {} = {}'.format(n,i,(n*i)))
        sleep(0.5)

