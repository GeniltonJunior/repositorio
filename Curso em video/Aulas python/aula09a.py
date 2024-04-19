frase = 'Curso em Video Python'
print(frase)
print(frase[3]) #fatiamento de unidade
print(frase[3:13]) #fatiamento com apontamento de inicio e fim
print(frase[:13]) #fatiamento sem apontamento de inicio
print(frase[1:15:2]) #fatiamento pulando unidades
print(frase[::2]) # fatiamento pulando unidades sem apontamento de inicio e fim
print(frase.count('o')) #conta quantas unidades destacadas existem dentro da str
print(frase.upper()) #joga todos os caracteres da str para maiusculo
print(frase.lower())#joga todos os caracteres da str para minusculo
print(len(frase)) #conta quantas unidades compoem a str
#frase.strip some com os espaços nas extremidades da frase
#frase.rstrip some com os espaços a direita da frase
#frase.lstrip some com os espaços a esquerda da frase
print(frase.replace('Python', 'Android')) #altera str antiga pela nova mas não salva
print('Python' in frase) #verifica se a unidade pedida esta dentro da str
print(frase.find('Curso')) #mostra a posição que em que a unidade selecionada esta dentro da str
print(frase.find('curso')) # devolve o valor de -1 se não existir a unidade selecionada dentro da str
