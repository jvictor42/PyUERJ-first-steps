#Aula 8 exercicio 4 apostila
#  O método de Newton para raiz quadrada. Suponha que você queira calcular a raiz quadrada de n. Se você começar com quase qualquer aproximação, poderá calcular uma aproximação melhor (mais próxima da resposta real) com a seguinte fórmula: melhor = (approx + n/approx)/2

print('O método de Newton para raiz quadrada.')
z=int(input('Digite o número para tirar raiz: '))
def newton_raiz(n):
    disc=1
    approx=n/2
    while disc > 0.001:
        melhor=(approx+n/approx)/2
        disc= melhor - approx
        if disc < 0:
            disc*=-1
        approx = melhor
        print(melhor)

if z<0:
        print('Não serve para raiz imaginária. Coloque um número positivo!')
else:
    print(newton_raiz(z))
    
