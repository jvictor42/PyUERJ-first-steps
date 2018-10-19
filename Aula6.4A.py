#Aula 6  exercicio 4 da apostila
#Desenhe um quadrado, usando a forma de tartaruga, ao invés da flecha, para desenhar. Mude a velocidade com que a tartaruga faz o desenho

import turtle
jn=turtle.Screen()
joana=turtle.Turtle()
teca=turtle.Turtle()
luna=turtle.Turtle()
john=turtle.Turtle()

joana.color("red")
teca.color("green")
luna.color("pink")
john.color("blue")

joana.shape("turtle")
teca.shape("turtle")
luna.shape("turtle")
john.shape("turtle")

joana.speed(0)
teca.speed(10)
luna.speed(6)
john.speed(3)

for i in[1,2,3,3]:
    joana.forward(300)
    joana.left(90)
    teca.forward(300)
    teca.left(90)
    luna.forward(300)
    luna.left(90)
    john.forward(300)
    john.left(90)
