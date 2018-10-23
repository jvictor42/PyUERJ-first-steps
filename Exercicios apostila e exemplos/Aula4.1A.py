#Aula 4 Exercicio apostila
#ex 1--------------------------------
#exemplo ultimo-----------------------------
def do_twice(f):
    f ()
    f ()
def print_spaml (): 
    print('spam') 

do_twice (print_spaml)
print('Fim do exemplo.')

#PARTE 1(modificado) -----------------------------
print('Parte 1 -----------')
#Modifique do_twice para que sejam necessários dois argumentos, um objeto de função e um valor, e chame a função duas vezes, passando o valor como um argumento.
def do_twice(f,x):
    f (x)
    f (x)
def print_spam (x):
    print(x) 

do_twice (print_spam,2018)

#PARTE 2 (outra versão) ----------------------------
print('Parte 2 -----------')
#Escreva uma versão mais geral de print_spam, chamada print_twice, que use uma string como parâmetro e imprima duas vezes.
def do_twice(g,y):
    g(y)
    g(y)
def print_twice (y):
    print(y)
    print(y)
do_twice(print_twice,'spamm')

#PARTE 3 (outra versão) ----------------------------
print('Parte 3 -----------')
#Use a versão modificada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento. Defina uma nova função chamada do_four que recebe um objeto de função e um valor e chama a função quatro vezes, passando o valor como um parâmetro. Deve haver apenas duas declarações no corpo desta função, não quatro.
def do_twice(g,y):
    g(y)
    g(y)
def print_twice (y):
    print(y)
    print(y)
def do_four(g,y):
    do_twice(g,y)
    do_twice(g,y)
do_four(print_twice,'spam')
#resultado final da parte 3, imprime 8 vezes
print('Fim!')
