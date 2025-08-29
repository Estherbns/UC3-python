class Praia:
    def __init__(self, nome, distancia_centro, numero_veranistas, tipo_acesso):
        self.nome = nome
        self.distancia_centro = distancia_centro 
        self.numero_veranistas = numero_veranistas
        self.tipo_acesso = tipo_acesso 

    def __str__(self):
        return (f"Praia: {self.nome}\n"
                f"Distância do centro: {self.distancia_centro} km\n"
                f"Número de veranistas: {self.numero_veranistas}\n"
                f"Tipo de acesso: {self.tipo_acesso}")
    

    #praia1 = Praia("Praia do Sol", 12.5, 500, "carro")

   # print(praia1)
#-----------------------------------------------------------------------

lista= []

qtde_praia = int(input("Quantas praias informar?"))

for x in range(qtde_praia):
    nome_praia = input("nome da praia?")
    distancia_praia = int(input("distancia da praia do centro?"))
    media_veranista = int(input("Qtde de veranista?"))
    tipo_acesso = int(input("tipo de acesso : 1 = asfaltado / 2- não asfaltado"))

    objeto_praia = Praia(nome_praia,  distancia_praia, media_veranista , tipo_acesso)

    lista.append(objeto_praia)

   # numero de praia + de 15km do centro
    num_praia_15km = 0
    for item in lista:
        if item.distancia_centro >15 :
            num_praia_15km += 1

    
    # media  de veranistana ultima temporada

Qtde_praia = 0
soma_veraniata = 0
Qtde_media_asfalt = 0
  
for x in lista:
    if x.tipo_acesso ==0 :
        soma_veraniata += x.numero_veranistas
        Qtde_praia += 1
        Qtde_media_asfalt = soma_veraniata / Qtde_praia

print(f'numero de praia + de 15km do centro: {num_praia_15km}')
print(f'Media de veraninista por praia asfaltada: {Qtde_media_asfalt}')



    
