from math import(radians,sin,cos,tan)
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem SENO de {:.2f}\nO ângulo de {} tem COSSENO de {:.2f}\nO ângulo de {} tem TANGENTE de {:.2f}'.format(an,sen,an,cos,an,tan))

