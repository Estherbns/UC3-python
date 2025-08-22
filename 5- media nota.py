
while True:
    nome = input("informe o seu nome: ") 
    nota1 = float(input("informe nota1: "))
    nota2 = float(input("informe nota2: "))

    media = (nota1 + nota2)/2

    if media > 6.5:
        situacao= "Aprovado"
        
    # print(f'O aluno { nome} tem a média { media}  e está aprovada ' )

    else:
        situacao= "Reprovado"
        #print(f'O aluno { nome} tem a média { media}  e está reprovado ' )

    print(f'O aluno { nome} tem a média { media}  e está {situacao} ' )

    resp = input("deseja continuar incluir outro aluno? (s/n)")
    if resp == 'n' or resp == 'N':
        break # termina o while

    elif resp != 'n' or resp != 'N' or resp != 's' or resp != 'S': 
            print( "digite novamente S ou N")
            continue



