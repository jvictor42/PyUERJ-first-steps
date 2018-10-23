#Exercício 3 Aula 1
#Ache os zeros da função y = 3x^2 - 4x -10 
import math
a=3
b=-4
c=-10
delta=b**2-4*a*c
y1=(-b+(math.sqrt(delta)))/(2*a)
y2=(-b-(math.sqrt(delta)))/(2*a)
#Usei o pacote math, da aula 2. math.sqrt(x)=raiz quadrada de x
#Apresentação dos resultados
print('Ache os zeros da função y = 3x^2 - 4x -10')
print('Y1=',y1,' e Y2=',y2)
print('Fim!')
