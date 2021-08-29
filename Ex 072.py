contagem = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE',
            'QUATORZE','QUINZE','DEZESSEIS','DEZESETE','DEZOITO','DEZENOVE','VINTE')
x = int(input('Digite um número de 0 até 20: '))
while x not in range(0,21):
    x = int(input('Tente novamente.Digite um número de 0 até 20: '))
print('Você digitou {}'.format(contagem[x]))
