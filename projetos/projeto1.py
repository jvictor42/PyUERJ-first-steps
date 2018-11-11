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

#Funções pẽndulo de mola. Os parametros x_0 e v_0 não representam os iniciais do sistema, mas os anteriores na contagem. 
def aceleracaoX(k,m,r_mod,xn,l0,v_mod):
    an_x = -(k/m)(1-(l0/r_mod)+(v_mod/r_mod)**2)*xn
    return an_x
def velocidadeX(var_t,t0,n,v_0,an_x):
    vn_x = v_0 +an_x*var_t
    return vn_x
def posicaoX(var_t,x_0,vn_x):
    xn = x_0+vn_x+var_t
    return xn

#Definindo as listas vazias
list_z = []
list_x = []
list_velz = []
list_velx = []
list_mod_vel = []
list_time = []
list_r_mod = []
list_a_mod = []

#Usuário
print('Entre com os parametros do problema.')
mass = float(input(' Massa do objeto: '))
kons = float(input(' Constante elastica da mola: '))
lnat = float(input(' Comprimento natural da mola: '))
print('Quais coordenadas de posição inicial do pêndulo?')
x_ini = float(input('Em x: '))
list_x.append(x_ini)
z_ini = float(input('Em z: '))
list_z.append(z_ini)
print('Qual intervalo de tempo de oscilação?')
t_ini = float(input(' tempo inicial: '))
list_time.append(t_ini)
t_fin = float(input(' tempo final: '))

#Estrutura sequencial
a_cont=0
v_cont=0
r_cont=0

cond='s'
condu = input('Deseja ir para o pêndulo simples? s/n')

'''if cond == condu:
    print('##### Solução do movimento de um pêndulo simples #####')'''
    
