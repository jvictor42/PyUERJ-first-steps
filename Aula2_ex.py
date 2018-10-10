# Aula 2 exemplos - Variáveis, expressões e declarações
#Os tipos de valores (letra: string / número: inteiro, float, bool)
type('letras')
type(1.0)
type(10)
type('10')
#Definir variáveis e buscar o tipo
mensagem='Temos muitos alunos na discipline'
n_aluno=25
pi=3.1415926535897932
type(mensagem)
type(n_aluno)
type(pi)
#OBS: Variáveis tem que começar com letras, não pode ter caracteres especiais e não pode ser uma palavra chave
#500mil_pessoas = 'multidao' (SyntaxError) pq ñ começa com letra
#milh@res = 10000            (SyntaxError) pq ñ pode ter carac. espec.
#class = 'Introdução a Python' (SyntaxError) pq é palavra chave class
#Listar as palavras chaves
import keyword
print(keyword.kwlist)
