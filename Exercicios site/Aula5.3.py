#Aula 5 exercicio 3 site
#Multiplicar todos os numero de uma lista
n=int(input('quantos numeros deseja multiplicar? '))

def inputNS(m):
    s=1
    for i in range(m):
        j=float(input('digite numero número: '))
        s=j*s
    return (s)
print('O resultado do produto é ',inputNS(n))      
print('Fim!')
        
