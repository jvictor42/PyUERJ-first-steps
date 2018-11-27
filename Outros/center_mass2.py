#programa Center Massa 2
import math
def c_m(l1,l2):
    soma_pesos = sum(l1)
    prod_pp=0
    for (i,valor) in enumerate(l1):
        prod_pp = prod_pp+ l1[i]*l2[i]
    cm = prod_pp/soma_pesos
    return cm

full = []
l=[1]
name = input('Nome do arquivo de extrassão: ')
arq = open('/home/JackS/data/'+name+'.txt','r')
while len(l) !=0:
	l = arq.readline()
	if len(l) != 0:
		l = l.replace ( "\n", "" ) 
		l = l.replace ( "  ", " " ) 
		l = l.split(' ')
		for n in l:
			full.append(float(n))
	else:
		print('foi')
		break

full_splitted = [full[i::3] for i in range(3)]
listx = full_splitted[0]
listy = full_splitted[1]
listL = full_splitted[2]

pos_x = c_m(listL,listx)
pos_y = c_m(listL,listy)
print('Centro de Luminosidade x={} e y={}'.format(pos_x,pos_y))
