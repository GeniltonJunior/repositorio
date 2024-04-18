cidade = input('Digite sua cidade: ')
cidade2 = input('Digite a cidade que quer visitar: ')
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('se em {0} temperatura é de {2}ºC na cidade de {1} ela correspode a {3}ºF!'.format(cidade, cidade2,c,f))