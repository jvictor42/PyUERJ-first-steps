#Aula 6 exercicio 6 apostila + funções extra!
#Crie uma nova função para generalizar a anterior, que tome como parâmetro o numero de pontas da estrela (ou sol) e a cor do desenho. Generalize a função ainda mais, para dar como parâmetro a posição inicial do lápis.
import turtle
jn=turtle.Screen()
jn.title("Estrela")
jn.bgcolor("MidnightBlue")

star=turtle.Turtle()
star.shape("turtle")
star.speed(6)
star.pensize(2)
star.hideturtle() 

def drawing_stars(name,p,c,x,y):
    name.penup()
    name.setpos(x,y)
    name.pendown()
    name.color(c)
    name.begin_fill() 
    for n in range(p): 
        if n % 5==0:
            name.left(45)
            name.left(144)
            name.forward(100)
        else:
            name.left(144)
            name.forward(100)            
    name.end_fill()
    
drawing_stars(star,5,"red",-200,200)    
