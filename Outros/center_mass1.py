#programa Centro de Massa 1
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
cond = 0
name = input('Nome do arquivo de extrassão: ')
arq = open('/home/JackS/data/'+name+'.txt','r')
while cond !=1:
	l = arq.readline()
	l = l.replace ( "\n", "" ) 
	l = l.replace ( "  ", " " ) 
	l = l.split(' ')
	cond = len(l)
	if cond !=1:
		listx.append(float(l[0]))
		listy.append(float(l[1]))
		listL.append(float(l[2]))
	else:
		break
		
	
pos_x = c_m(listL,listx)
pos_y = c_m(listL,listy)
print('Centro de Massa x={} e y={}'.format(pos_x,pos_y))



