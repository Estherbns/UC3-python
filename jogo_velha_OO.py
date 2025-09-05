
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


