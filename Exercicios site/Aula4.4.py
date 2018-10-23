#Aula 4 exercicio 4 site 
#Modifique a função anterior para retornar uma tupla (tuple) ordenada, onde o primeiro elemento seja o menor e o segundo o maior.
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
def lista(x,y):
    if x>=y:
        l1=[y,x]
        print(l1)
    if y>x:
        l2=[x,y]
        print(l2)
lista(n1,n2)
print('fim!')
