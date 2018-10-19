#Aula 6  exercicio 2 da apostila
#Faça modificações similares para permitir que o usuário mude a cor da tartaruga durante a execução do programa
import turtle
jn=turtle.Screen()
rubinho=turtle.Turtle()
rubinho.pensize(4)

print('Insira cores')
a=input('primeira cor: ')
b=input('segunda cor: ')
c=input('terceira cor: ')
d=input('quarta cor: ')

for i in[a,b,c,d]:
    rubinho.color(i)
    rubinho.forward(300)
    rubinho.left(90)
jn.title("Hoje não!")
