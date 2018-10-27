#Aula 6 exercicio 6 apostila + funções extra!
#Desenhe uma estrela de 5 pontas. Encapsule numa definição de função para este desenho.
import turtle
jn=turtle.Screen()
jn.title("Estrela")
jn.bgcolor("MidnightBlue")

star=turtle.Turtle()
star.color("white")
star.shape("turtle")
star.speed(0)
star.pensize(2)
star.hideturtle() 

def drawing_stars():
    star.begin_fill() 
    for n in range(5): 
        star.left(144)
        star.forward(100)
    star.end_fill()

drawing_stars()    
