class Calcular ():
    def __init__(self, numero1, numero2 ):
        self.numero1 = numero1  
        self.numero2 = numero2
        self.total = 0 
    
    def somar(self):
        self.total =  self.numero1 + self.numero2

    def subtrair(self):
        self.total =  self.numero1 - self.numero2
    
    def multiplicar(self):
       self.total =  self.numero1 * self.numero2

   # def dividir(self, var1, var2): # nesse caso qdo não for  definir variavel no inicio do init
   #    self.total =  self.numero1 -  self.numero2
       
    def dividir(self): 
      self.total =  self.numero1 -  self.numero2




      