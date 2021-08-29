from time import sleep
def maior(* num):
    total = grande = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for i in num:
        print(i,end=' ',flush=True)
        total += 1
        sleep(0.3)
        if i>grande:
            grande=i

    print(f'Total de números = {total}')
    print(f'O maior valor informado é {grande}')


maior(9,6,3,4,5,6,2)
maior(6,2,1)
maior(0,5,8,6,2,1)
maior(2,4)