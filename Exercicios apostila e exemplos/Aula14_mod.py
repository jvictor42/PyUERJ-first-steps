#Aula 14 exercicio 3
#Transformando em modulo.

def read_files(name,par):
	arq = open(name,'r')
	line = arq.readlines()
	cut = line[0].strip().split(par).copy()  #usado no try
	size = len(cut)
	dicionary = {}
	for i in range(size):
		#i=i+1
		dicionary[i]=[]
	for l in line:
		l = l.strip().split(par)
		for (i,valor) in enumerate(l):
			#i=i+1
			try:
				dicionary[i].append(float(valor))
			except:
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
	return dicionary

if __name__ == '__main__':
			
	cond2='s'
	while cond2=='s':
		try:
			nm= input('Digite o nome do arquivo|tabela. ') 
			par = input(' Tipo de espaçamento ')
			print(read_files(nm),par)
			break
		except:
			print('\nArquivo não existe ou nome inválido.')	
			cond2=input('Tentar de novo? [s/n] ')
