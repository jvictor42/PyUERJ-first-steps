#Aula 4 exercicio 2 site + extra
#Crie uma função usando a palavra chave for para fazer as repetições ao calcular o fatorial de un numero inteiro maior ou igual a 1
print('Fatorial de 5')
def fat(n):
    if n==0:        #if, else são condições. Condições verdadeiro ou falso.
        return(1)
    if n==1:
        return(1)
    if n>1:
        for i in range(n):
           n=fat(n-1)*n
           return (n)
print(fat(5))
    
#Usando a função fatorial no módulo math: (MODO FÁCIL)
import math
h=int(input('Digite um num. inteiro que se deseja o fatorial: '))
fato = math.factorial(h)
print('O fatorial de ',h,' é',fato)

#Usando while e outras condições.

m=int(input('Digite outro num. inteiro que se deseja o fatorial: '))
f=1
print('Resolvendo {}!='.format(m), end='') #o comando .format(m) substitui o espaço vazio {} pela variavel m. O end='' , evista que o programa pule de linha.
while m>0: #Enquanto o contador foir maior que m.
    f*=m #Isso é o mesmo que f=f*m
    m-=1 #Isso é o mesmo que m=m-1
print('{}'.format(f))
print('Fim!')
