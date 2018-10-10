# Exercício 3 Aula 3
#Crie uma funcão para calcular o ángulo zenital do sol (da semana passada) tomando como argumento as medidas da altura e o comprimento da sombra.
print('Ângulo zenital do sol cuja sombra de um poste de 5m, tem 50cm.')
import math
def ang_zen(x,y):
    teta=math.degrees(math.atan(x/y))
    print(teta)
    
print(ang_zen(0.5,5), 'angulo zenital')
print('Fim!')
