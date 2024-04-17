produto = float(input('Qual o valor do produto?: '))
avista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 8 / 100)
print('O produto no valor de R${:.2f} sai no valor de R${:.2f} se for a vista, ja se for parcelado sai no valor de R${:.2f}'.format(produto,avista,parcelado))