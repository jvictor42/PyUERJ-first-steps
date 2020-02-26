class  MeuTempo : 
    # Métodos previamente definidos aqui ... 
    def  __init__ ( self ,  hrs = 0 ,  mins = 0 ,  segs = 0 ): 
        """ Criar um novo objeto MeuTempo inicializado para hrs, min, segs. 
           Os valores de mins e segs podem estar fora do intervalo de 0-59, 
           mas o objecto MeuTempo resultante será normalizado.  """ 
        # Calcular total de segundos para representar 
        self.totalsegs =  hrs * 3600  +  mins * 60  +  segs 
        self.horas =  self.totalsegs  //  3600         # Divisão em h, m, s 
        restosegs =  self.totalsegs  %  3600 
        self.minutos  =  restosegs  //  60 
        self.segundos  =  restosegs  %  60
        if self.horas >=24:
            self.horas = self.horas%24
    def  to_seconds ( self ): 
        "" "Retorna o número de segundos representados por esta instância " "" 
        return  self.totalsegs
    
    def  __add__ ( self ,  other ): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o simbolo + """
        return  MeuTempo ( 0 ,  0 ,  self.to_seconds()  +  other.to_seconds())
    
    def __str__(self):
        """Retorna uma representação do objeto como string, legível para humanos."""
        return '%.2d:%.2d:%.2d' % (self.horas, self.minutos, self.segundos)

    def __sub__ (self, other):
        """Retorna a subtração do tempo atual e outro, para utilizar com o simbolo - """
        return  MeuTempo ( 0 ,  0 ,  self.to_seconds()  -  other.to_seconds())

    def  depois ( self ,  time2 ): 
        "" "Retorna True se self for estritamente maior que time2" "" 
        if  self.horas  >  time2.horas : 
            return  True 
        if  self.horas  <  time2.horas : 
            return  False 

        if  self.minutos  >  time2.minutos : 
            return  True 
        if  self.minutos  <  time2.minutos : 
            return  False 
        if  self.segundos  >  time2.segundos : 
            return  True 
        return  False

    def depois2 (self , other):
        return self.totalsegs > other.totalsegs #forma mais rápida de fazer em uma linha o método depois.

    def entre(self,t1,t2):
        if t1.totalsegs<= self.totalsegs <t2.totalsegs:
            return True

        elif t2.totalsegs <= self.totalsegs <t1.totalsegs:
            return True
    
        else:
            return False

    def entre2(self,t1,t2):
        if self.__gt__(t1) and self.__lt__(t2):
            return True

        if self.__gt__(t2) and self.__lt__(t1):
            return True

        else:
            return False

	
	
        
