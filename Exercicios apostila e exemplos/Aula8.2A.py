#Aula 8 exercicio 2 apostila
# Modifique a função counter para contar o número de vezes que os dígitos 0 e 5 aparecem em um dado número n. Por exemplo, n = 10568, tem 2 dígitos 0 ou 5.
print('Contador')
m=int(input('digite o número para contagem: '))

def counter(n):
    count = 0
    while n!=0:
        if n % 5==0:
            count = count + 1
            n = n // 10         # divisão de inteiros
            n=int(n)
        else:
            n = n // 10         # divisão de inteiros
            n=int(n)

    return count

print('Tem {} dígitos 0 ou 5.'.format(counter(m)))
    
