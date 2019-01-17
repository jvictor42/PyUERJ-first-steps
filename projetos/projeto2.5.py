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
def eletron_momentum(a,b,theta):
       d = (a**2 + b**2 - 2*(a*b)*math.cos(math.radians(theta)))**0.5
       d = round(d,3)
       return d

def efect_compton(theta,E1,Ep):
	e2 = E1*Ep/(Ep+E1*(1-math.cos(math.radians(theta))))
	e2 = round(e2,3)
	return e2

def plot_graf(listcomp, namex, namey, labelname, part):
    cont = 0
    for n in range(cond1):
        lx = listcomp[cont] ; ly = listcomp[(cont + part)]
        plt.plot(lx,ly , label = labelname + str(n))
        plt.xlabel(namex)
        plt.ylabel(namey)
        cont = cont + 5
    plt.title('Effect Compton ')
    plt.legend()
    plt.show()
    plt.savefig("grafico.png")
    plt.close()

def add():
	lc.append(l1) ; lc.append(l2) ; lc.append(l3) ; lc.append(l4) ; lc.append(l5)

#----------Definindo as listas de dados------------------------------- 
lc = []      #lista composta
ll = []      #lista dos lambdas
llabel = ["\u03B8 (°)", "Collision ", "Energy \u03B3 (MeV)", "Energy e⁻ (MeV)","Momentum e⁻ (MeV)"]

#-----Apresentação ---------
print('\n','\n')
print(7*' '+'Colisões Relativística \nby José Victor, Thaís Guerini and Gustavo Borges.   ','     © Jacks coorp \n')
print('Gerador pseudoaleatório de espalhamento Compton \nSistema de unidades naturais c=1 e h=1\n') 
cond1 = int(input('Insira o número de colisões:  '))

now = datetime.now()
limit = now.minute + now.second
if limit <cond1:
	limit = limit + cond1
elif (limit - cond1) <10:
	limit = (limit + 20)

for i in range(cond1):
        l1 = [] ; l2 = [] ; l3 = [] ; l4 = [] ; l5 = [] #listas auxiliares
        p = randint(1,limit)/10
        f1 = particle(0,p)
        e1 = particle(0.511,0)
        l2.append(f1.fourmoment()) ; theta=0
        while theta <= 360:
                E2 = efect_compton(theta,f1.E,e1.E) ; E2 = round(E2,3)
                f2 = particle(0,E2)
                pe = eletron_momentum(f1.E,f2.E,theta) ; pe = round(pe,3)
                e2 = particle(0.511,pe)
                l1.append(theta) ; l3.append(f2.E) ; l4.append(e2.E) ; l5.append(e2.p)		
                theta = theta + 1 ; theta = round(theta,3)
        add()
#------Gráfico----------- 
cond2 = 's'
while cond2 == 's':
	print('Escolha um dos gráficos:\n')
	for i in range(2,5):
		nn = i -1
		print('[{}] = {} X {}'.format(nn,llabel[i],llabel[0]))	   
	cont2 = int(input('Escolha: ')) ; cont2= cont2 + 1
	plot_graf(lc, llabel[0],llabel[cont2],llabel[1], cont2)
	cond2 = input('Deseja ver outro gráfico? [s/n] ')
print('Bye')

		
