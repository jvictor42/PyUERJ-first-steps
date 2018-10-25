#Aula 5 exercicio 4 site
#Escreva uma função em Python para verificar se um número está em um determinado intervalo.
n=int(input('Digite um número: '))

def verify(m):
    s1=(m-3)
    s2=(m+3)
    print('{} está entre [{},{}].'.format(m,s1,s2))
verify(n)   
print('Fim!')
