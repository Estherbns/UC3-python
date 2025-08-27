palavra = "rinoceronte"
lista = []

#exercicio de lista

for indice  in range(len(palavra)): # range é especifico do python. Começando por 0
     
     #print(palavra[indice])
     lista.append(palavra[indice])
     print(lista)


     # ou então. O for sabe ler uma lista

for i in palavra:
     lista.append(i)
