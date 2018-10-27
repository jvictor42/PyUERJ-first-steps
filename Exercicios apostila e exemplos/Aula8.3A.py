#Aula 8 exercicio 3 apostila
# Encapsule e generalize a seguinte declaração:

'''for i in [12, 16, 17, 24, 29]:
       if i % 2 == 1:  # If the number is odd
       break        #  ... immediately exit the loop
    print(i)
print("done")'''

#Para encapsular, basta transformar em uma função. Para generalizar, basta tirar a particularidade da função e tornar generalizada.

def break_odd(n):
    for i in n:
        if i % 2 == 1:  # If the number is odd
            break        #  ... immediately exit the loop
    return(i)
print(break_odd(x))  #x é a variavel lista que será associado a função.
