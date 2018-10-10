#Funções matemáticas
#exemplo 1--------------------------------
print('ex.1 - Funções matemáticas')
import math
cateto_oposto = 4
cateto_adjacente = 2
tangente_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tangente_theta) #resultado em radianos
print(theta, 'em radianos')
angle=math.degrees(theta) #transforma de radianos pra graus
print(angle, 'em angulo')
#é possivel transformar em graus usando relação matemática conhecida ao invez da função
theta_cal=theta*180/math.pi
print(theta_cal,'resultado calculado')
#exemplo 2--------------------------------------------------
print('ex.2 - Qual ângulo teta, correspondente a cosseno(teta)=raiz(2)/2 ?')
teta=math.degrees(math.acos(math.sqrt(2)/2))
print(teta, 'em angulo, exercicio')
#exemplo 3--------------------------------------------------
#COMPOSIÇÃO
print('A ideia desse exemplo 3 é juntar os argumentos de outras funções e mostrar que pode ser qualquer tipo de expressão')
x=math.sin(angle/(360.0*2*math.pi))
x=math.exp(math.log(x+1)) #repare que o x é função e argumento da função
print(x, 'valor')
#exemplo 4--------------------------------------------------
#ADICIONANDO FUNÇÕES NOVAS
print('ex.4 - Adicionando novas funções')
def print_poema():
    print('Caminante, no hay camino,')
    print('se hace camino al andar.')

def verso_poema():
    print('Caminante, son tus huellas')
    print('el camino y nada más;')
    
    print_poema()
    
    print('Al andar ser hace el camino,')
    print('y al volver la vista atrás,')
    print('se ve la senda que nunca')
    print('se ha de volver a pisar')
    print('Caminante no hay camino')
    print('sino estelas en la mar')
    
verso_poema()
