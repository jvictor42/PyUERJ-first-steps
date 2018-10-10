# Exercício 2 Aula 3
#Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial, a final e o tempo transcorrido para um objeto em MRU. Também crie uma funcão que calcule e imprima a velocidade de um objeto a partir da aceleração constante e o tempo (MRUA) (p.ex. queda libre). 
def print_vmedio(x0,x,t):
    v=(x-x0)/t
    print(v)
print('Calculando velocidade média e velocidade de queda de um corpo')  
print(print_vmedio(3,10,5), 'velocidade média em m/s')

def print_acel(a,t,t0):
    V=a/(t-t0)
    print(V)

print(print_acel(9.8,5,0), 'Velocidade do corpo em queda livre')
print('Fim!')
