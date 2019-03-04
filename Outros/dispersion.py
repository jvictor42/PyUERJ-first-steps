#Programa em desenvolvimento.
#Cria gráficos de dispersão e ajusta a melhor reta, a partir de arquivos txt ou xlsx.
import sys
import matplotlib.pyplot as plt
import numpy as np               
from matplotlib.animation import FuncAnimation
import csv
from openpyxl import load_workbook

def best_fit(X,Y,leg):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    a = numer / denum
    b = ybar - a * xbar

    print('best fit line for {}:\ny = {:.3f} + {:.3f}x'.format(leg,b, a))

    return a, b

def plot_graf(l1,l2,l3, namex, namey, system):
    lx = np.array(l1) ; ly = np.array(l2)
    if len(l3) !=0:
        lY = np.array(l3)
        T1 = (lx,ly) ; T2 = (lx,lY)
        k = (T1,T2)
        cor = ("blue", "green")
        forma= ("o","^")
        labelk = ("Full","B.K")
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        bf2 = best_fit(list1,list3,'B.K')
        yfit2 = [bf2[1] + bf2[0] * xi for xi in lx]
        plt.plot(lx, yfit2, c= 'grey', marker ='4')
        for data, color, group, markers in zip(k,cor,labelk,forma):
            x, y  = data
            ax.scatter(x, y, alpha=0.8, c=color,marker = markers, edgecolors='none', s=30, label=group)
        plt.legend(loc=1)
    else:
        plt.scatter(lx,ly,c = 'green', marker = 'o')
    yfit = [bf[1] + bf[0] * xi for xi in lx]
    plt.plot(lx, yfit, c= 'Black')
    plt.xlim([1, 2])
    plt.ylim([38, 42])
    plt.xlabel(namex)
    plt.ylabel(namey)
    plt.title(system)
    plt.show()
    plt.savefig("grafico.png")
    plt.close()

def read_files(name,par):
    arq = open(name+'.txt','r')
    line = arq.readlines()
    for n in line:
        n = n.strip().replace(',', '.').split(par)
        if n[0] and n[1] !='0':
            list1.append(float(n[0]))
            list2.append(float(n[1]))
        if len(n) == 3 and n[2]!='0':
            list3.append(float(n[2]))

def read_xlsx(name,n,L_n):
    wb = load_workbook(name+'.xlsx')
    sheet = wb.active
    interval = input('Intervalo da coluna {} '.format(n))
    for cell in sheet[interval]:
        if cell[0].value !='0':
            L_n.append(float(str(cell[0].value).replace(',', '.')))

print(3*' '+'Programa estatístico - Ajuste da reta\n',
      'Extensões suportadas:\n[1] ".txt"\n[2] ".xlsx"')
cond = 's'
while cond == 's':
	list1 =[] ; list2= [] ; list3= []
	tab = input('Nome do arquivo ')
	cond1 = input('Escolha a extensão do arquivo de entrada: ')
	if cond1 =='1':	
		par = input('Parametro ')
		read_files(tab,par)
	elif cond1 =='2':
		cond2=input('Dupla dispersão?[s/n] ' )
		lc=[list1,list2,list3]
		for n, L_n in enumerate(lc,1):
			if n!=3: read_xlsx(tab,n,L_n)
			if n==3 and cond2=='s': read_xlsx(tab,n,L_n)
				
	else: break
	bf = best_fit(list1,list2,'Full')
	plot_graf(list1,list2,list3,'Log(\u03C3)','Log(L)','Relação L-\u03C3')
	cond = input('Gerar novo gráfico? [s/n] ')
	print('\n')
