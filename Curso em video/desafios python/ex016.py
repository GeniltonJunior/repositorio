from math import(trunc , ceil , floor)
num = float(input('Digite um valor: '))
print('O valor digitado foi {}\nA porção inteira é {}\nO arredondamento para cima é {}\neo arredondamento para baixo é {}'.format(num,trunc(num),ceil(num),floor(num)))