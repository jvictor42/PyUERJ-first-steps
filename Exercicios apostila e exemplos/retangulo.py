#Classe retangulo completa

from ponto import * 
class retangulo:
	"""Representa um retangulo. 
	atributos: 
	- largura, do tipo float
	- altura, do tipo float 
	- canto, do tipo Ponto."""
	'''def __init__(self, x=0, y=0):
		self.x=x  #self é uma palavra chave. Dentro dela mesma.
		self.y=y'''

	def largura(ponto,x):
		l = float(ponto.x + x)
		return l

	def altura(ponto,y):
		h = float(ponto.y + y)
		return h
	
	def canto(ponto):
		c = ponto
		return c

	def area_r(ponto,x,y):
		A = retangulo.largura(ponto,x) * retangulo.altura(ponto,y)
		return A
