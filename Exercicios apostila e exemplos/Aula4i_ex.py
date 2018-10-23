#Aula 4 exemplos de importação de modulos
#É possivel importar um módulo INTEIRO/COMPLETO com:
import math #import (nome do módulo)
print(math)
print(math.pi)
print(math.sin(45))
#Repare q você fica preso ao comando math. pra chamar uma função.

#Ou é possivel importar só uma função do pacote
from math import pi
from math import sin
print(pi)
print(sin(45))
#repare que você não fica preso ao math., chamando apenas com o nome da função.

#Porem, para não ter que chamar uma a uma, se usar * é como chamar o modulo inteiro. E de quebra Ñ FICA PRESO ao math.
from math import  *
print(sin(pi/3))
print('Fim!')
