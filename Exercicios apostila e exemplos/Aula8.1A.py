#Aula 8 exercicio 1 apostila
#conjectura de Collatz, diz que "Todos os inteiros positivos irão eventualmente convergir para 1 usando as regras do Collatz"
print('Teste da conjectura de Collatz')
n=int(input('digite um número: '))

def collatz(x):
    c=0
    while x != 1:
        c+=1
        print('contagem {}.'.format(c))
        if x%2==0:
            x=x/2
        else:
            x=x*3+1
    return(x)
print('resultado {}. A conjectura está correta.'.format(collatz(n)))
