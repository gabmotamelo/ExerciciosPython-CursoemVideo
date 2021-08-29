num = int(input('Digite um número inteiro: '))
print('[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL')
conv = int(input('Digite a base de conversão(1/2/3): '))
if conv == 1:
    print('O número {} convertido para BINÁRIO será {} '.format(num , bin(num)))
elif conv == 2:
    print('O número {} convertido para OCTAL será {} '.format(num , oct(num)))
elif conv == 3:
    print('O número {} convertido para HEXADECIMAL será {} '.format(num , hex(num)))