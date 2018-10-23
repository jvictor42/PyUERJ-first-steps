#Aula 6 exercicio 6 apostila + funções extra!
#Fazer 4 estrelas.
import turtle
jn=turtle.Screen()
jn.title("4 stars!!!")
jn.bgcolor("MidnightBlue")

star=turtle.Turtle()
star.color("white")
star.shape("turtle")
star.speed(0)
star.pensize(2)
star.hideturtle() #essa função faz a Turtle ficar "invisivel".

#Podemos criar uma função para desenhar estrelas

def drawing_stars():
    star.pendown() #essa função coloca a caneta no papel
    star.begin_fill() #essa função pinta formas fechadas
    for n in range(5): 
        star.left(144)
        star.forward(100)
    star.end_fill()
    star.penup() #Essa função levanta a caneta do papel. Assim podemos mudar a posição da tartaruga entre estrelas sem marcar com linhas o caminho.

#Agora é só definir a posição das estrelas

for i in range(4):
    drawing_stars()
    star.left(90)
    star.forward(300)
