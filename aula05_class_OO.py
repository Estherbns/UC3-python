# primeira implementação
class Exemplo:
    pass # para qdo ainda não tem ideia do conteudo

x = Exemplo() # instancia ( acho eu )

#segundo exemplo de class
class Cachorro():
    def __init__(self, raca = "viralata"): # vem por defaault viralata se não for informado a raça 
        self.raca = raca
        self.idade = 10

    #def __str__(self)
    #    print("eu sou cachorro")


cachorro = Cachorro("labrador") # geralmente atributo eh minusculo. E a classe a primrira letra em maiuscula
cachorro2 = Cachorro("pudle")
cachorro3 = Cachorro()

print(cachorro.idade)
print(cachorro.raca)
