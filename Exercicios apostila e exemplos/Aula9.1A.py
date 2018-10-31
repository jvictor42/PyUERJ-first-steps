#Aula 9 Exercicio 1 apostila
#Resolução numérica de equações diferenciais. Imagine que tem um/a maratonista treinando, que num trecho de $5 km$ tem velocidade quase constante de $12 km/h$. Produza uma lista distância percorrida em intervalos de 1 minuto.
print('Lista de distâncias percorridas em 12km/h a cada 1min')
cam=5
vel=12
def min_hora(min):
    h=min/60
    return(h)
def dist(t,v):
    dmin=v*t
    return(dmin)
    
dist_list=[]
dm=0
while dm <= 5:
    dm=dist(min_hora(1),vel)+dm
    dist_list.append(dm)
print(dist_list, end=' ')
print('fim')
