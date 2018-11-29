#programa Centro de luminosidade (pixel)
#Esse Script funciona em conjunto com a tabela de distribuição de pixel, feita na tarefa listpix na formatação (%d %d), do pacote IRAF.
import math
def c_m(l1,l2):
    soma_pesos = sum(l1)
    prod_pp=0
    for (i,valor) in enumerate(l1):
        prod_pp = prod_pp+ l1[i]*l2[i]
    cm = prod_pp/soma_pesos
    return cm

listx=[]
listL=[]
listy=[]
name = input('Nome do arquivo de extrassão: ')
arq = open('/home/JackS/data/'+name+'.txt','r')
line = arq.readlines()  
for l in line:
	l = l.strip().replace ( "  ", " " ).split(' ')
	listx.append(float(l[0]))
	listy.append(float(l[1]))
	listL.append(float(l[2]))
	
pos_x = c_m(listL,listx)
pos_y = c_m(listL,listy)
print('Centro de Luminosidade x={} e y={}'.format(pos_x,pos_y))


