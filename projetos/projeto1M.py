#PROJETO 1M 
#Nesse projeto criei um programa que resolve numericamente um pendulo de mola e um pendulo simples.

#Módulos usados ----------
import math
import matplotlib.pyplot as plt

#----------Definindo as funções-----------------------
#Função que gera arquivo de saida --------
def table_txt(l_generic,l_nomes,name):
	'''Essa função permite a criação de arquivos de saida txt, com nome definido pelo usuário'''
    arq = open(name+".txt","w")
    for n in l_nomes:
        arq.write(2*' '+ n +' ')
    arq.write('\n')
    for (i,valor) in enumerate(l_generic):
        arq.write(2*' '+ str(s1[i])+2*' '+ str(s2[i])+2*' '+ str(s3[i]) +2*' '+ str(s4[i])+2*' '+ str(s5[i])+2*' '+ str(s6[i])+2*' '+ str(s7[i])+2*' '+ str(s8[i]))
        arq.write('\n')
    arq.close()

#Função modulo e angulo---------------------
def modulo(g1,g2):
    '''Essa função calcula o módulo de um vetor genérico, usando a equação:\n
            |G| = sqrt(G1² + G2²)        '''
    g_mod = math.sqrt(g1**2 + g2**2)
    return g_mod

def teta_degrees(x_0,z_0):
    '''Função que calcula o angulo em função da posição do objeto em um instante de tempo.'''
    teta=0
    if z_0<=0: #quadrante 4 e 3
        teta = math.atan(x_0/z_0)
    elif x_0<=0 and z_0>0: #quandrante 2 
        teta = math.atan(z_0/x_0) - math.pi/2
    elif x_0>=0 and z_0>0: #quadrante 1 
        teta = math.pi/2 + math.atan(z_0/x_0)
    teta1=math.degrees(teta)
    list_te.append(teta1) #LEMBRAR DE TIRAR
    return teta

#Funções pẽndulo de mola. Os parametros g_0 e gn são genéricos. 
def aceleracao(k,m,r_mod,l0,v_mod):
    '''Função aceleração do pêndulo sem definição de direção'''
    an = -(k*(r_mod-l0)/m+(v_mod**2)/r_mod)
    return an
def incremento(var_t,g_0,pn):
    '''Função genérica de incremento. Soma o termo anterior a um novo, realizado em um pequeno intervalo de tempo.'''
    gn = g_0 + pn*var_t
    return gn

#Função dos gráficos----------------
def plot_graf(listax,listay,nomex,nomey):
	plt.plot(listax,listay)
	plt.xlabel(nomex)
	plt.ylabel(nomey)
	plt.show()
	plt.close()

#Definindo as listas de dados, master(aninhada) e labels------------------------------- 
list_te = [] #LEMBRAR DE TIRAR
s1=list_z = []
s2=list_x = []
s3=list_velz = []
s4=list_velx = []
s5=list_mod_vel = []
s6=list_time = []
s7=list_mod_raio = []
s8=list_mod_acel = []
list_master = [s1,s2,s3,s4,s5,s6,s7,s8]
list_label = ["Eixo Z(m)","Eixo x(m)","Vel. z(m/s)","Vel. x(m/s)", "Modulo velocidade(m/s)","Tempo(s)","Posição(m)","Aceleração(m/s²)"]

#Função adiciona lista-------------------
def list_ad(l1,l2,l3,l4,l5,l6,l7,l8):
    list_z.append(l1)
    list_x.append(l2)
    list_mod_raio.append(l3)
    list_velz.append(l4)
    list_velx.append(l5)
    list_mod_vel.append(l6)
    list_time.append(l7)
    list_mod_acel.append(l8)

#-----------Usuário------------------------
print('\n','\n')
print('       Programa numérico pendulo        \n',
      'by José Victor    ','     © Jacks coorp \n', 
      '##### Solução do movimento de um pêndulo de mola #####')
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

#Estrutura sequencial-------------------
ax=0
az=0
t_cont=0
velx=0
velz=0
g=9.780318   #no nivel do mar
dt=0.05      #variação de tempo

while t_cont<=t_fin:
    velx = incremento(dt,velx,ax)             #incremento em Vx
    velz = incremento(dt,velz,az)             #incremento em Vz
    x_ini = incremento(dt,x_ini,velx)         #incremento em X
    z_ini = incremento(dt,z_ini,velz)         #incremento em Z
    m_raio = modulo(x_ini,z_ini)              #modulo do raio
    m_vel = modulo(velx,velz)                 #modulo da velocidade
    m_acel = modulo(ax,az)                    #modulo da aceleração
    t_cont = t_cont + dt                      #contador de tempo
    list_ad(z_ini,x_ini,m_raio,velz,velx,m_vel,t_cont,m_acel) #adiciona nas listas
    theta=teta_degrees(x_ini,z_ini)                           #Angulo no instante t+n*dt
    ax = aceleracao(kons,mass,m_raio,lnat,m_vel)*(math.sin(theta)) #acel. em x
    az = - g - aceleracao(kons,mass,m_raio,lnat,m_vel)*(math.cos(theta)) #acel. em z

#Interação gráfica------------------
cond1=input('Deseja visualizar no gráfico? [s/n]: ')
while cond1=='s': 
	print('Escolha entre as opções abaixo: ')
	for (i, valor) in enumerate(list_label):
	    print(i, valor)
	opx=int(input('Eixo x '))
	opz=int(input('Eixo z '))
	plot_graf(list_master[opx], list_master[opz], list_label[opx], list_label[opz])	
	cond1=input('Deseja visualizar outro gŕafico? [s/n]: ')

#Saida dos dados ---------------------------	
cond2=input('Deseja salvar os resultados em arquivo? [s/n] ')
if cond2=='s':
	n_arq=input('Nome do arquivo de saida: ')
	table_txt(list_x,list_label,n_arq)
print('Bye')

'''#if cond == condu:
    print('##### Solução do movimento de um pêndulo simples #####')'''
    
