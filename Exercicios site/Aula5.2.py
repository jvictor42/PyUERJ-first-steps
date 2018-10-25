#Aula 5 exercicio 2 site
#somar todos os numero de uma lista
n=int(input('quantos numeros deseja somar? '))

def inputNS(m):
    s=0
    for i in range(m):
        j=float(input('digite numero número: '))
        s=j+s
    return (s)
print('O resultado da soma é ',inputNS(n))      
print('Fim!')
