def meuverso(palavras): #definiu a função com parametro	
    print(palavras)
    print(palavras)     #Escreveu o que precisa ser feito, no caso print 2 vezes do parametro
    
def minhacancao(verso1, verso2): #cria uma nova função com 2 parametros agora
    meuverso(verso1)
    meuverso(verso2)  #define as instruções, porem a instrução é a função dita antes.
    
minhacancao("lalarí","lalará")  #chama a segunda função mas definindo valores pros parametros.

#REPARE: da pra criar funções com o mesmo parametro, pq uma vez executada a função, ela "desaparece".
def meuverso(palavras):  
    print(palavras)
    print(palavras)
    
def minhacancao(verso1, verso2):
    meuverso(verso1)
    meuverso(verso2)
    
minhacancao("naaaaa na na nana nanaa","tudum tudum dum")

#POREM eu poderia só chamar a função, mudando o argumento dos parametros.
minhacancao("ha " *3, "ho "*3)

#Agora eu to definindo uma variavel c, depois chamo ela como parametro da função meuverso.
c = "I want to ride my bicycle"
meuverso(c)

#agora definindo outra função TENTANDO usar a primeira função dentro.
def gato_duplo (parte1, parte2): 
    gato = parte1 + parte2 
    #a=variavel_qualquer
    meuverso (gato) #REPARE QUE essa linha de comando não executa a primeira função. Isso pq quando cria uma variavel dentro da função, ela é local e existe apenas dentro da função. Porem estão associadas agora.

#print(a)--> essa linha de comando daria erro no codigo, pq mesmo que definida dentro da função, ela só existe pra auxiliar na execução da mesma.

#Agora se definirmos duas variaveis, podemos associa-las aos parametros de uma função existente.
linha1 = "blim "
linha2 = "blem! "
gato_duplo(linha1,linha2) #linha1=parte1 e linha2=parte2

#print(gato)--> Se tentarmos imprimir a variavel gato, da erro. Após a execusão da função a ariavel é destruida.
linha1= "miau"
linha2= "grrr miau"
gato_duplo(linha1,linha2)
#Se atribuir à uma variavel o resultado de uma função vazia, pode receber um valor "None"
resultado = meuverso("under pressure")
print(resultado)
print(type(resultado))
print('Fim!')
