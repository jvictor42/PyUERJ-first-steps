#Aula 7 exercicio 1 apostila
import turtle
def draw_bar(t, height,col):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           
    t.color("blue", col)
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             
   # t.forward(1)

wn = turtle.Screen() 
wn.title("Histograma")        
wn.bgcolor("pink")

tess = turtle.Turtle()      
tess.pensize(3)
c ='s'
while c=='s':
    xs =int(input('Frequencia: ')) 
    k=input('Cor da barra: ')
    draw_bar(tess,xs,k)
    c=input('Continuar? [s/n]... ')
print('Bye.')

#wn.mainloop()
