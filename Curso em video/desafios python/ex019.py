from random import choice
n1 = str(input('Primeiro funcionario: '))
n2 = str(input('Segundo funcionario: '))
n3 = str(input('Terceiro funcionario: '))
n4 = str(input('Quarto funcionario:'))
n5 = str(input('Ultimo funcionario:'))
lista = [n1, n2, n3, n4 ,n5]
escolhido = choice(lista)
print('O funcionario escolhido foi {}!'.format(escolhido))