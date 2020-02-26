#projeto 2
#Nesse projeto trabalhamos com colisões relativística. Especificamente no do espalhamento compton. Um caso de colisão relativística eslástica.

#-----Modulos e classes ---------
from particula import *
from random import *
from datetime import datetime   #usaremos os minutos e os segundos para impor limites a aleatóriedade.
import math
import matplotlib.pyplot as plt
import numpy as np               
from matplotlib.animation import FuncAnimation 

#----------Definindo as funções-----------------------
c = 1
def law_cosines(theta,a,b):
	d = (a**2 + b**2 - 2*(a*b)*math.cos(theta))**0.5
	d = round(d,3)
	return d

def efect_compton(theta,E1,Ep):
	e2 = E1*Ep/(Ep+E1*(1-math.cos(theta)))
	e2 = round(e2,3)
	return e2

def plot_graf(listx,listy,namex,namey,colision):
	plt.plot(listx,listy)
	plt.xlabel(namex)
	plt.ylabel(namey)
	plt.title('Efeito Compton - '+colision+'MeV/c')
	plt.show()
	plt.close()

def add_clear(l1,l2,l3,l4):
	lc.append(l1) ; lc.append(l2) ; lc.append(l3) ; lc.append(l4)
	l1 = [] ; l2 = [] ; l3 = [] ; l4 = []

#----------Definindo as listas de dados------------------------------- 
l1 = []      # Theta
l2 = []      #4momento foton 1
l3 = []      #4momento foton 2
l4 = []      #4momento eletron 2
lc = []      #lista composta
llabel = ["Theta (rad)", "foton E=","foton 2 (MeV/c)","eletron (MeV/c)"]

#-----Apresentação ---------
print('\n','\n')
print(7*' '+'Colisões Relativística \nby José Victor, Thaís Guerini and Gustavo Borges.   ','     © Jacks coorp \n')
print('Gerador pseudoaleatório de espalhamento Compton') 
cond1 = int(input('Insira o número de colisões:  '))

now = datetime.now()
limit = now.minute + now.second
if limit <cond1:
	limit = limit + (1,5*cond1)
elif (limit - cond1) <12:
	limit = limit + 48

for i in range(cond1):
	p = randint(1,limit)
	f1 = particle(0,p)
	e1 = particle(0.511,0)
	l2.append(f1.fourmoment()) ; theta=0
	while theta <= math.pi:
		E2 = efect_compton(theta,f1.E,e1.E) ; E2 = round(E2,3)
		f2 = particle(0,E2/c)
		pe = law_cosines(theta,f1.p,f2.p) ; pe = round(pe,3)
		e2 = particle(0.511,pe)
		l1.append(theta) ; l3.append(f2.fourmoment()) ; l4.append(e2.fourmoment())		
		theta = theta + math.pi/10 ; theta = round(theta,3)
	add_clear(l1,l2,l3,l4)

#------Gráfico----------- provisório pra testar. Resolver o lance da lista lc[2] vir em tupla e foder o gráfico
plot_graf(lc[0], lc[2], llabel[0],llabel[2],llabel[1]+str(lc[1][0][0]))	
		
