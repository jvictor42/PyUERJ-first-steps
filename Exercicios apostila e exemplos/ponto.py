#Aula 16
class ponto:
	def __init__(self, x=0, y=0):
#__int__ é o nome da variavel especial do python, assim como o main uasdo em modulo.
		'''cria um novo ponto posicionado na origem'''
		self.x=x  #self é uma palavra chave. Dentro dela mesma.
		self.y=x
#DICA: from ponto import * 

	def distancia_da_origem(self):
		""" Calcula minha distânica da origem """
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5
	def ponto_medio(self, alvo):
		""" Retorna o ponto medio entre esse ponto e o alvo """
		mx = (self.x + alvo.x)/2
		my = (self.y + alvo.y)/2
		return ponto(mx, my) #retorna a propria claase, um objeto que é um ponto
	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)
