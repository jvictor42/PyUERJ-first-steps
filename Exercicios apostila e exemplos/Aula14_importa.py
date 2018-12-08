#Aula 14 exercicio 4
#importa o modulo.
import Aula14_mod as al
import matplotlib.pyplot as plt
import numpy as np

nome = input('Digite o nome do arquivo|tabela. ')
par = input('Tipo de espaçamento. ')
dicio = al.read_files(nome,par)
print(dicio)

n_bins = 13  #largura da coluna
fig, axs = plt.subplots(1,len(dicio), sharey=True, tight_layout=True)
for (n,valor) in enumerate(dicio):
	#plt.xlabel(valor)
	axs[n].hist(dicio[valor], bins=n_bins)
plt.show()
