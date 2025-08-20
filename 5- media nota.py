
nome = input("informe o seu nome: ") 

nota1 = float(input("informe nota1: "))
nota2 = float(input("informe nota2: "))
media = (nota1 + nota2)/2
if media>= 6.5:
    
    print(f'O aluno { nome} tem a média { media} anos e está aprovada ' )

else:
    print(f'O aluno { nome} tem a média { media} anos e está reprovado ' )


