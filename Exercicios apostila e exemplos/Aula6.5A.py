#Aula 6 exercicio 5 apostila + funções extra!
#Fazer uma estrela. Extra um circulo em volta.
import turtle
jn=turtle.Screen()
jn.title("Pentagrama!!!")
jn.bgcolor("MidnightBlue")

star=turtle.Turtle()
star.color("red")
star.shape("turtle")
star.speed(3)
star.pensize(2)
star.hideturtle() #essa função faz a Turtle ficar "invisivel".

ball=turtle.Turtle()
ball.color("DarkRed")
ball.shape("turtle")
ball.speed(4)
ball.pensize(4)
ball.hideturtle() 
ball.setpos(-50,-36) #essa função muda a posição inicial da turtle

for n in[1,2,3,4,5]: #Isso ou usar o comando range como mostrado abaixo
    star.left(144)
    star.forward(100)

for m in range(360): #esse range é otimo quando a lista tem muitos elementos
     ball.left(1)
     ball.forward(1)
