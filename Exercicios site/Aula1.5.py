#Exercício 5 Aula 1
#Calcule o seu IMC = M/A^2 (com a massa em Kg e a altura em metros). Um valor saudável estara --em geral-- entre 20-25. Um bebê de 6 meses "gorducho" tem 70 cm de "comprimento" e 11 kg de massa, qual o IMC dele?
Mb=11
Ab=0.7
IMCb=Mb/(Ab**2)
print('O IMC do bebê é ',IMCb)
print('Agora e o seu?')
#Resolvi testar o comando input.
M=input('Entre com sua massa: ')
print()
M=float(M)
A=input('Entre com sua altura: ')
print()
A=float(A)
IMC=M/(A**2)
print('Seu IMC é: ',IMC)
print('Fim, seu gordo')
#TypeError: can't multiply sequence by non-int of type 'str' line 13
