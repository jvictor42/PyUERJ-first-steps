#PROJETO 1
print('##### Solução do movimento de um pêndulo de mola #####')
#Devemos pedir que o usuário coloque os valores de k,x0,l0. O intervalor de tempo deve ser definido pelo usuário.

#Módulos usados ----------
import math
import matplotlib.pyplot as plt
import turtle

#Definindo as funções:
g=9.780318   #no nivel do mar
dt=0.05      #variação de tempo

#Funções modulo
def mod_acel(a_x,a_y):
    a_mod = math.sqrt(a_x**2 + a_y**2)
    return a_mod

def mod_vel(v_x,v_y):
    v_mod = math.sqrt(v_x**2 + v_y**2)
    return v_mod

def mod_raio(x_0,y_0):
    r_mod = math.sqrt(x_0**2 + y_0**2)
    return r_mod

#Funções pẽndulo de mola. Os parametros x_0 e v_0 não representam os iniciais do sistema nem o eixo, mas os anteriores na contagem. 
def aceleracao(k,m,r_mod,xn,l0,v_mod):
    an = -(k/m)*(1-(l0/r_mod)+(v_mod/r_mod)**2)*xn
    return an
def velocidade(var_t,v_0,an):
    vn = v_0 +an*var_t
    return vn
def posicao(var_t,x_0,vn):
    xn = x_0+vn*var_t
    return xn

#Definindo as listas 
list_z = []
list_x = []
list_velz = []
list_velx = []
list_mod_vel = []
list_time = []
list_mod_raio = []
list_mod_acel = []

#Função adiciona lista
def list_ad(l1,l2,l3,l4,l5,l6,l7,l8):
    list_z.append(l1)
    list_x.append(l2)
    list_mod_raio.append(l3)
    list_velz.append(l4)
    list_velx.append(l5)
    list_mod_vel.append(l6)
    list_time.append(l7)
    list_mod_acel.append(l8)

#Usuário
print('Entre com os parametros do problema.')
mass = float(input(' Massa do objeto em kg: '))
kons = float(input(' Constante elastica da mola em N/m: '))
lnat = float(input(' Comprimento natural da mola em m: '))
print('Quais coordenadas de posição inicial do pêndulo em m?')
x_ini = float(input('Em x: '))
z_ini = float(input('Em z: '))
print('Qual intervalo de tempo de oscilação em segundos?')
####t_ini = float(input(' tempo inicial: '))
t_fin = int(input(' tempo final: '))

#Estrutura sequencial
ax=0
az=0
t_cont=0
velx=0
velz=0

for i in range(0,t_fin):
	if t_cont <= t_fin:

	    velx = velocidade(dt,velx,ax)
	    velz = velocidade(dt,velz,az)
	    x_ini = posicao(dt,x_ini,velx)
	    z_ini = posicao(dt,z_ini,velz)
	    m_raio = mod_raio(x_ini,z_ini) #modulo do raio
	    m_vel = mod_vel(velx,velz)     #modulo da velocidade
	    m_acel = mod_acel(ax,az) #modulo da aceleração
	    t_cont = t_cont + i*dt #contador de tempo
	    list_ad(z_ini,x_ini,m_raio,velz,velx,m_vel,t_cont,m_acel) #adiciona nas listas
	    ax = aceleracao(kons,mass,m_raio,x_ini,lnat,m_vel) #acel. em x
	    az = - g - aceleracao(kons,mass,m_raio,z_ini,lnat,m_vel) #acel. em z
	
'''cond='s'
condu = input('Deseja ir para o pêndulo simples? s/n ')

if cond == condu:
    print('##### Solução do movimento de um pêndulo simples #####')'''
    
