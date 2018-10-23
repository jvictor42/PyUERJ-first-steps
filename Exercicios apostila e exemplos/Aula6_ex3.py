import turtle
# a ideia desse é fazer um quadrado com um lado de cada cor
jn=turtle.Screen()
joana=turtle.Turtle()

for i in["yellow", "blue","green","red"]:
    joana.color(i)
    joana.forward(300)
    joana.left(90)

