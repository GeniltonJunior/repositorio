from random import shuffle
n1 = str(input('Digite o nome dos seu amigos e descubra a ordem de quem vai pagar um churrasco : '))
n2 = str(input('Segundo amigo: '))
n3 = str(input('Terceiro amigo: '))
n4 = str(input('Quarto amigo: '))
n5 = str(input('Ultimo amigo: '))
lista = [n1,n2,n3,n4,n5]
shuffle(lista)
print('A ordem dos amigos a pagar ficou: {}'.format(lista))