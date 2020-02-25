#PROJETO 2
#Criando classe 4momento.

c=2.99792458e8  #Em m/s
m=9.10938e-35 #Em kg
mev=1.6022e-13 # Em Joule

class fourmoment:
	def __init__(self, E=0, p=0):
		'''Cria um vetor quadrimomento, para uma particula generalizada.'''
		self.p=p		
		self.E=E

	def __str__(self):        
		return "({0}, {1})".format(self.E, self.p)

	def energy(self):
		return ((self.p*c)**2 + (m*(c**2))**2)**0.5

class foton(fourmoment):
	def __init__(self, p=0):
		'''cria um foton. Deve ser atribuido um valor de momento'''
		self.p=p		
		self.E=p*c

class eletron(fourmoment):
	def __init__(self, p=0):
		'''cria um eletron no repouso se não for atribuido valores de momento'''
		self.E=self.energy()
		self.p=p




