#Aula 5 exercicio 6 site
#Escreva uma função em Python para verificar se um número é perfeito ou não. Na teoria dos números, um número perfeito é um inteiro positivo que é igual à soma de seus divisores positivos apropriados, isto é, a soma de seus divisores positivos excluindo o próprio número (também conhecido como sua soma de alíquotas).
n=int(input('Digite um número positivo '))
y=0
def nperfect(x):   
    for i in range(1,x):
        m=i
        if x % m == 0:
            y=y+m
        if y==n:
            print('{} É um número perfeito'.format(n))
if n>0:
    nperfect(n)
else:
    print('Não é positivo')
print('Fim!')

