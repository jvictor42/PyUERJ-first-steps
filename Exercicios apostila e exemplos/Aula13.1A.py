#Exercicio da 1 aula 13
#tilizando um arquivo de dados com várias colunas (por exemplo, o arquivo dados_alunos.txt), faça um histograma com os dados de cada uma das colunas. Dica: utilize o matplotlib para fazer os histogramas.
import matplotlib.pyplot as plt
import numpy as np

def histograma(l1,l2,l3):
	'''N_points = 100000'''
	n_bins = 15  #largura da coluna
	x = l1
	y = l2
	z = l3
	fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

	axs[0].hist(x,'age', bins=n_bins)
	axs[1].hist(y, bins=n_bins)
	axs[2].hist(z, bins=n_bins)
	plt.show()
	
list_age = []
list_height = []
list_weight = []
arq = open('dados_alunos.txt')
linhas = arq.readlines()
for l in linhas:
	l = l.strip().split('\t')
	list_age.append(float(l[0]))
	list_height.append(float(l[1]))
	list_weight.append(float(l[2]))

histograma(list_age,list_height,list_weight)


