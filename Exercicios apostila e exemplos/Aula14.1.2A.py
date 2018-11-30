#Exercicio 1 e 2 Aula 14
#Lê um arquivo de n colunas. Separa as colunas em listas e atribui keys, para cada coluna. Criar um comando contra falha do usuário.

def read_files(name):
	arq = open(name,'r')
	line = arq.readlines()
	cut = line[0].strip().split('\t').copy()  #usado no try
	size = len(cut)
	dicionary = {}
	for i in range(size):
		#i=i+1
		dicionary[i]=[]
	for l in line:
		l = l.strip().split('\t')
		for (i,valor) in enumerate(l):
			#i=i+1
			dicionary[i].append(valor)
	#------ As proximas linhas modificam o dicionário no caso da tabela possuir cabeçalho.
	cond = cut[0]
	try:
		cond = int(cond)
	except:
		dicionary2 = {}
		for (i,valor) in enumerate (cut):
			#i=i+1
			del(dicionary[i][0])
			dicionary2[valor]=dicionary[i]
		dicionary = dicionary2
	#---------------------------------------------------		
	return dicionary
cond2='s'
while cond2=='s':
	try:
		nm= input('Digite o nome do arquivo|tabela. ') 
		print(read_files(nm))
		break
	except:
		print('\nArquivo não existe ou nome inválido.')	
		cond2=input('Tentar de novo? [s/n] ')
