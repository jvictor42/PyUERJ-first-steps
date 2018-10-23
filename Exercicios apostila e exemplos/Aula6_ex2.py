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

teca.pensize(3) #muda a largura da linha 

teca.forward(50)
teca.left(120)
teca.forward(50)
teca.left(120)
teca.forward(50)
teca.left(80)

joana.forward(50)
joana.left(90)
joana.forward(50)
joana.left(90)
joana.forward(50)
joana.left(90)
joana.forward(50)

jn.mainloop() #mantem o programa em suspenso até fechar a janela

#--------- Repare que esse programa tem muitas repertições. Poderiamos ter colocado um loop.

#usando looop

for i in [0,1,2,3]:  #para fazer um loop, criamos uma lista [  ] e usamos o comando "for"
    luna.forward(50)
    luna.left(90)

for m in [0,1,2]:
    john.forward(50)
    john.forward(120)



