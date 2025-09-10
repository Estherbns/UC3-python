
import random # é uma função interna do puthon

class Velha():
    def __init__(self):
        # lista
        self.lista0 = [["   ", "   ", "   "] , ["   ", "   ", "   "], ["   ", "   ", "   "]] # 3 lista dentro de uma lista "maior"        


    def Desenhar(self):
        print( ""+ self.lista0[0] [0]+  "|"+ self.lista0[0] [1]+ "|"+ self.lista0[0][2]+ "")
        print( "___ ___ ___")
        print( ""+ self.lista0[1] [0]+  "|"+ self.lista0[1] [1]+ "|"+ self.lista0[1][2]+"")
        print( "___ ___ ___")
        print( ""+ self.lista0[2] [0]+  "|"+ self.lista0[2] [1]+ "|"+self.lista0[2][2]+"")

    def jogarMaquina(self):
     return random.randint(0, 2)
    
    def verificarVencedor(self):
       dicVencedor = {}

       for i in["X", "O"]: # for que ler lista
          # testar horizontal
          dicVencedor[i] = (self.lista0[0][0] == self.lista0[0][1] == self.lista0[0][2] == i )
          dicVencedor[i] = (self.lista0[1][0] == self.lista0[1][1] == self.lista0[1][2] == i ) or  dicVencedor[i]
          dicVencedor[i] = (self.lista0[2][0] == self.lista0[2][1] == self.lista0[2][2] == i ) or  dicVencedor[i]

           # testar verticaç
          dicVencedor[i] = (self.lista0[0][0] == self.lista0[1][0] == self.lista0[2][0] == i ) or  dicVencedor[i]
          dicVencedor[i] = (self.lista0[0][1] == self.lista0[1][1] == self.lista0[2][1] == i ) or  dicVencedor[i]
          dicVencedor[i] = (self.lista0[0][2] == self.lista0[1][2] == self.lista0[2][2] == i ) or  dicVencedor[i]

           # testar diagonal
          dicVencedor[i] = (self.lista0[0][0] == self.lista0[1][1] == self.lista0[2][2] == i ) or  dicVencedor[i]
          dicVencedor[i] = (self.lista0[0][2] == self.lista0[1][1] == self.lista0[2][0] == i ) or  dicVencedor[i]
       

       return dicVencedor 
    
    def verificarEspaco(self):
       espaco = False

       for x in range(3):
          for y in range(3):
             if self.lista0[x][y] == "" :
                espaco = True
                return espaco 
      
       return espaco 
          