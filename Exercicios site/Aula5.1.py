#Aula 5 exercicio 1 site
#Selecionar o maior entre 3 numeros inseridos
a=float(input('Insira o primeiro número: '))
b=float(input('Insira o segundo número: '))
c=float(input('Insira o terceiro número: '))

def select(x,y,z):
    if x>=y and z:
        print('{} é maior que {} e {}.'.format(x,y,z))
    else:
        if y>z:
            print('{} é maior que {} e {}.'.format(y,x,z))
        else:
            print('{} é maior que {} e {}.'.format(z,x,y)) 
select(a,b,c)
print('Fim!')
