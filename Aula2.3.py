# Exercício 3 Aula 2
#Suponha que o preço de um livro seja 24.95 reais, porém as livrarias têm desconto de 40%. Os custos de envio são de 3.00 reais para o primeiro livro e 0.75 reais para os livros adicionais. Qual é o custo total da compra de 60 livros?

pç=24.95
envio_ad=0.75
n=60
desc=0.4
pp1=pç*n*(1-desc)+3+(n-1)*envio_ad #desconto só no livro
pp2=(pç*n+3+(n-1)*envio_ad)*(1-desc) #desconto na compra toda

print('Qual valor a pagar em uma compra de 60 livros, custando R$24.95, aplicando desconto de 40%, cujo envio é R$3.00 + R$0.75 a cada livro adicional?')
print('R$',pp1,' se o desconto for só no livro')
print('R$',pp2,' se o desconto for em tudo')
print('Fim!')
