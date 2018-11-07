#Aula 10 exercicio 2 apostila 
#Crie uma lista com números sequenciais com incrementos de uma unidade, de 1 até 10000. Dica: use a função range.
print('Lista de elemontos de 1 até 10000')

contl = []
cont = 0
for i in range (0,10000):
	cont = cont + 1
	contl.append(cont)
print(contl)
print('Fim!')
