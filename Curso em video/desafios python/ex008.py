medida = float(input('Uma distancia em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {:.0f} m corresponde a {} km, {} hm, {} dam, {:.0f} dm, {:.0f} cm, {:.0f} mm ' .format(medida,km,hm,dam,dm,cm,mm))