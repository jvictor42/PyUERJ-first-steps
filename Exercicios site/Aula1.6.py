#Exercício 6 Aula 1
#Calcule a velocidade final de um objeto em queda livre a partir de 3 metros de altura (sem resistencia do ar). Calcule o tempo que esse objeto demora para cair.
import math
g=9.8
d=3
v0=0
v=math.sqrt(v0**2+(2*g*d))
t=g/v
#apresentação dos resultados
print('Calcule a velocidade final de um objeto em queda livre a partir de 3 metros de altura (sem resistencia do ar). Calcule o tempo que esse objeto demora para cair')
print('Velocidade ao chegar no solo é ',v,'m/s, em ',t,'s')
print('Fim!')
