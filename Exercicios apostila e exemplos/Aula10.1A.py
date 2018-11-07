#Aula 10 exercicio 1 apostila
#Considere a função abaixo. Esse tipo de função é considerada uma função modificadora pois modifica o objeto que é passado como argumento.

def dobrar_elementos(uma_lista):
    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais.
    """
    for (i, valor) in enumerate(uma_lista):
        novo_elem = 2 * valor
        uma_lista[i] = novo_elem

    return uma_lista

minha_lista = [2, 4, 6]
print(minha_lista)

dobrar_elementos(minha_lista)
print(minha_lista)

print('a) Modifique a função para retornar uma nova lista, sem modificar a lista usada como parâmetro. Esse tipo de função é chamado de função pura.')

def triplica_elementos(outra_lista):
    clone = outra_lista[:] #USANDO UMA LISTA CLONE
    for (i, valor) in enumerate(clone):
        novo_elem = 3 * valor
        clone[i] = novo_elem
    print(clone)
    return clone
    

minha_lista = [2, 4, 6]
print(minha_lista)

triplica_elementos(minha_lista)
print(minha_lista)

print('b) Modifique a documentação de ajuda da nova função, de tal forma que quando se chame a função help da nova função, se obtenha a descrição adequada.')

def triplica_elementos(outra_lista):
    """Essa função triplica os valores de uma lista, sem alterar a original. Abraços!"""
    clone = outra_lista[:] #USANDO UMA LISTA CLONE
    for (i, valor) in enumerate(clone):
        novo_elem = 3 * valor
        clone[i] = novo_elem
    print(clone)
    return clone
        

print('Usa o help da função triplica_elementos')


