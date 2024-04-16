real = float(input('Quanto dinheiro voce tem na carteira ?: R$ '))
dolar = real / 5.480
euro = real / 5.597
arg = real * 163.934
print('Com {:.2f} reais voce pode comprar U${:.2f}, {:.2f} euros e {:.2f} Pesos Argentinos '.format(real,dolar,euro,arg))