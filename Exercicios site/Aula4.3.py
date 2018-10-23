#Aula 4 exercicio 3 site + extra
#Crie uma função que compare 2 números e imprima na tela o resultado da comparação (a maior do que b, a menor do que b ou iguais) e retorne o valor do maior deles.
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
def comp(x,y):
    if x>y:
        print('{} é maior.'.format(x))
    if y>x:
        print('{} é maior.'.format(y))
    if x==y:
        print('{} e {} são iguais.'.format(x,y))
comp(n1,n2)
print('fim!')
