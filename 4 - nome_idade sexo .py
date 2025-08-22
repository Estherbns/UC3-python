

nome = input("informe o seu nome: ") 

idade = int(input("informe sua idade: "))

sexo = input("informe o seu sexo ( Masculino / Feminimo): ") 


if sexo.upper() == "FEMININO" : # upper transforma o texto todo em mausculo
    genero ='F'

elif sexo.upper() =="MASCULINO" : 
     genero ='M'

elif sexo != 'FEMININO' or sexo != 'MASCULINO' : 
   print( "Genero incorreto. Digite novamente o sexo (Masculino / Feminimo) ")


print(f'A pessoa :{ nome} tem { idade} anos e é do genero { genero} ' )

      

