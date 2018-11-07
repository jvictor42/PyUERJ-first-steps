# Aula 9 Exercicio 2 apostila
# Queremos obter uma tabela ou gráfico da distância percorrida en função do tempo e o tempo total para chegar em 7 km, faça isto utilizando listas.
print('Lista de distâncias percorridas por uma corredora a cada 1min')
cam = 5
vel = 12

def min_hora(minu):
    h = minu / 60
    return(h)

def dist_cons(t, v):
    dmin = v * t
    return(dmin)

dist2 = 0.2
vel2 = 15
def dist_var(t,v0,v):
    dvar = (t/2)*(v-v0)
    return(dvar)

dist_list = []
dm = 0
while dm <= 7:
    if dm <=5:
        dm = dist_cons(min_hora(1), vel) + dm
        dist_list.append(dm)
        #print('1')
    if dm > 5 and dm < 5.2:
        dm = dist_var(min_hora(1),vel,vel2)
        dist_list.append(dm)
        #print('2')
    if dm >= 5.2:
        dm = dist_cons(min_hora(1), vel2) + dm
        dist_list.append(dm)
        print('3')
print(dist_list)
print('fim')

'''import matplotlib.pyplot as plt

plt.plot(xxxxxxx,dist_list)
plt.xlabel("tempo min")
plt.ylabel("distância km")
plt.show()
plt.close()'''

