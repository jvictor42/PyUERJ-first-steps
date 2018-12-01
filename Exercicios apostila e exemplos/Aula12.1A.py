#Aula 12 exercicio apostila Dicionários
#Utilizando dicionários e o método get, contrua a seguinte matriz em python e acesse os valores de índices (0,3), (2,1), (4,3) e (2,2).

def access():
	print('Acesse um termo da matriz: ')
	n = int(input('Digite a linha: ', ))
	m = int(input('Digite a coluna: ', ))
	termo = matriz.get((n,m))
	print(termo)

matriz = {}
cond=0
for i in range(1,6):
	for j in range(1,6):
		if i==1 and j==4:
			cond = cond + 1
			matriz[(i,j)] = cond
	
		if i==3 and j==2:
			cond = cond + 1
			matriz[(i,j)] = cond

		elif i==5 and j==4:
			cond = cond + 1
			matriz[(i,j)] = cond

		else:
			matriz[(i,j)] = 0
print(matriz)

logical = 's'
while logical == 's':
	access()
	logical = str(input('Deseja acessar algum item da matriz? s ou n \n'))
