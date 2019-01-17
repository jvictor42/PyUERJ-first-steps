#PROJETO 2
#Criando classe particula.

class particle:
    def __init__(self, m=0, p=0):
        '''Cria um cria uma particula com massa e momento igual a zero.'''
        self.p=p		
        self.m=float(m)
        self.E=self.energy()

    def energy(self):
        '''Energia relativistica da particula'''
        return ((self.p)**2 + (self.m)**2)**0.5

    def fourmoment(self):
        '''Vetor quadrimomento da particula'''
        return (self.E , self.p)

    def __str__(self):        
        return "({0}, {1})".format(self.m, self.p)
    
    def wave(self):
        return 1/self.p
