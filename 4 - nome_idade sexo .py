nome = input("informe o seu nome: ") 

idade = int(input("informe sua idade: "))

sexo = input("informe o seu sexo ( Masculino / Feminimo): ") 


if sexo == "Feminino" or sexo == "feminino":
    genero ='F'

elif sexo =="Masculino" or sexo == "masculino": 
   genero ='M'
else : 
   print( "digite novamente o sexo")



print(f'A pessoa :{ nome} tem { idade} anos e é do genero { genero} ' )


