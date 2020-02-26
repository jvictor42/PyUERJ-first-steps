class  MeuTempo :

    def  __init__ ( self ,  hrs = 0 ,  mins = 0 ,  segs = 0 ): 
        "" "Criar um objeto MeuTempo inicializado para hrs, mins, segs" "" 
        self.horas  =  hrs 
        self.minutos  =  mins
        self.segundos  =  segs
	
    def __str__(self):
        return "{0}:{1}:{2}".format(self.horas,self.minutos,self.segundos)

	def  add_time ( t1 ,  t2 ): 

	    h  =  t1.horas  +  t2.horas 
	    m  =  t1.minutos  +  t2.minutos 
	    s  =  t1.segundos  +  t2.segundos 

	    if  s  >=  60 : 
		s  -=  60 
		m  +=  1 

	    if  m  >=  60 : 
		m  -=  60 
		h  +=  1
		
	    sum_t  =  MeuTempo ( h ,  m ,  s ) 
	    return  sum_t

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
