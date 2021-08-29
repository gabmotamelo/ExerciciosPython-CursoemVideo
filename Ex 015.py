km = float(input('Quantos km foram percorridos pelo carro?'))
dias = int(input('Por quantos dias foram alugado o carro? '))
preco = (60*dias) + (km*0.15)
print('O carro foi alugado por {} dias.\nO carro percorreu {} kilômetros.\nO custo total então será de R${:.2f} . '.format(dias , km , preco))