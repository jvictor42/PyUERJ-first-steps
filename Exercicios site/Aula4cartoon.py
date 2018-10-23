#Aula 4 extra

#Write a function that draws a grid like the following

def line1(x,y,z):
    print(x,y*3,x,y*3,x)

def line2(x,y,z):
    print(z*3)

def line3(x,y,z):   
    line1(x,y,z)
    line2(x,y,z)
    line2(x,y,z)
    line2(x,y,z)

def cartoon(x,y,z):
    line3(x,y,z)
    line3(x,y,z)
    line1(x,y,z)
#Resultado
print('Desenho:')
cartoon('+','-','|     ')
print('Fim!')
