#Aula 5 exercicio 5 site + extra!
#Escreva um programa em Python para imprimir os números pares de uma determinada lista. Do contrario é impar.
n=int(input('Digite quantos número: '))

def numPar(m):   
    for i in range(0,m):
        j=float(input('digite número: '))
        if j % 2==0:
            print('{} é par.'.format(j))
        else:
            print('{} é impar.'.format(j))   
numPar(n)
print('Fim!')

#OUTRA FORMA: usando o terceiro indice da função range(i,j,k), onde k é o passo da sequencia.
print('Para uma lista com limite já conhecido, de 0 a 40: ')
for i in range(0,40,2):  #Ou (2,41,2)
    print(i, end=' ')
print('Esses são pares entre 0 e 40')

print('Fim!!')
