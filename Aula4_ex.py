#Aula 4 exemplos
#exemplo 1--------------------------------
#exemplo ultimo-----------------------------
def do_twice(f):
    f ()
    f ()
def print_spaml (): 
    print('spam') 

do_twice (print_spaml)
#exemplo ultimo (modificado)-----------------------------
#Modifique do_twice para que sejam necessários dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um argumento.
def do_twice(f,x):
    f (x)
    f (x)
def print_spam (): #Não da pra usar isso pq precisa de um argumento
    print('spam') 

do_twice (print_spam)
#Escreva uma versão mais geral de print_spam, chamada print_twice, que use uma string como parâmetro e imprima duas vezes.
