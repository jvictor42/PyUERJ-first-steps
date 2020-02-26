#Classe circulo completa

from ponto import * 
class circulo:
	def __init__(self,x=0,y=0, r=0):

		'''Define o centro de uma circunférência'''
		self.x=x  
		self.y=y
		self.r=r
		centro = ponto(self.x,self.y)
		raio = self.r

	'''def __str__(self):        #Isso serve para imprimir o ponto e ñ o main....
		return "({0}, {1}, {2})".format(self.x, self.y, self.r)'''
		
