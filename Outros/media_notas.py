#PROGRAMA EXERCICIO 1 - MÉDIA DO ALUNO  (esse simboo '#' significa que essa linha é de comentário. Usado quando queremos escrever algo pra orientar quem está lendo o código e não atrapalha o funcionamento do programa.)

# O comando "for" , cria um loop. Todas as tarefas são realizadas até o fim e depois volta pro inicio. O "range(0,60) ou range(60)", define quantas vezes isso será feito. 60 pq são 60 alunos.

for n in range (0,60):   
    nome_aluno = input( 'Nome do aluno: ')   #nome_aluno é a variavel. Input é o comando que pede pro usuário o que está em entre '   '
    matricula = input( 'Matricula do aluno: ')
    materia = input( ' Qual a disciplina? ')
    nota1 = input('1ª nota: ')
    nota1 = float(nota1)         #Explicação no fim do arquivo.

    nota2 = input('2ª nota: ')
    nota2 = float(nota2)

    nota3 = input('3ª nota: ')
    nota3 = float(nota3)

    result_final = (nota1 + nota2 + nota3)/3   #Aqui a variavel result_final faz a conta da média.
    print(nome_aluno, ", matricula: ",matricula)   #O comando print, ele imprime na tela o que está dentro do ( ). No caso vai imprimir o nome e a matricula.
    print("Média final ",result_final)

    #Agora a gente cria condições. Por exemplo: se o carro é um fusca, de um tampa. Se não for, não faça nada
    if result_final>=7 and result_final<=9: #Se for maior ou igual a 7 e menor ou igual a 9 fazer...        
        print( 'Aprovado.')
    elif result_final >9:        #ou se for maior que 9...
        print('Aprovado no grupo de pesquisa.')
    else:
        print( 'Reprovado.')

#Observação: Repara que tem comandos que estão mais pra fora "esquerda" e outros pra dentro "direita". Isso se chama indexar. Pra funcionar a estrutura tem q ser essa. "For" do lado de fora e as coisas acontecendo dentro dele. Mesma coisa o if elif e else.

#Observação 2: Quando usamos input, o que vem é uma string. É tipo uma palavra, mesmo que seja um numero. Mas pra fazer contas, tem q ser numeros. Então pra vc dizer pro python que a palavra 10, 9, 1.5 e etc, é um número mesmo, vc transforma ele em numero usando float(  ).

		
