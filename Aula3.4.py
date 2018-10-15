#Aula 3 exercicio 4
from math import *

#Exercício de conversão de unidades para resolver o exercício da corrida

def milha_metro(milhas):

	m = milhas*1609.34
	return(m)

def metro_milha(m):

	milhas=m/1609.34
	return(milhas)

def horas_seg(h):

	seg = 60*60*h
	return(seg)

def minutos_hora(minute):

	h = minute/60 
	return(h) 

def ms_km(ms):

        km=ms*3.6
        return(ms)

#agora que as funções conversões foram definidas, só resolver o problema.
print('Se uma pessoa demora 30 minutos em 4 milhas, qual velocidade media em km/h ?')

s=horas_seg(minutos_hora(30))
ms=milha_metro(4)/s
print('Velocidade média = ',ms_km(ms),'Km')

print('tempo medio por kilometro?')

t=(1000*horas_seg(minutos_hora(30)))/milha_metro(4)
print(t,'horas a cada kilometro') 
print('Fim!')
