# Classe para um veiculo
class Veiculo:
    def __init__(self, tipo_veiculo, marca, modelo, ano, placa):
        self.marca = marca
        self.tipo_veiculo = tipo_veiculo
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.esta_disponivel = True # Atributo para controlar a disponibilidade
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"

    
    def reservar(self):
        if self.esta_disponivel:
            self.esta_disponivel = False
            print(f"O {self} foi reservado.")
        else:
            print(f"O {self} não está disponível.")

    
# Classe para o cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"

# Classe principal para a locadora
class Locadora:
    def __init__(self, nome):
        self.nome = nome
        self.frota = [] # Lista para armazenar os carros da locadora
        self.clientes = [] # Lista para armazenar os clientes

    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)
        print(f"veiculo {veiculo} adicionado à frota.")

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado.")

    def encontrar_veiculo_por_placa(self, placa):
        for veiculo in self.frota: 
            if veiculo.placa == placa:
                return veiculo
        return None # Retorna None se o carro não for encontrado

    def alugar_veiculo(self, placa_veiculo, cliente):
        veiculo = self.encontrar_carro_por_placa(placa_veiculo)
        if veiculo and cliente in self.clientes:
            veiculo.reservar()
        elif not veiculo:
            print("veiculo não encontrado.")
        else:
            print("Cliente não cadastrado.")

    def devolver_veiculo(self, placa_veiculo):
        veiculo = self.encontrar_carro_por_placa(placa_veiculo)
        if veiculo:
            veiculo.devolver()
        else:
            print("veiculo não encontrado.")

    def listar_veiculo_disponiveis(self):
        print(f"\nveiculo disponíveis na {self.nome}:")
        for veiculo in self.frota:
            if veiculo.esta_disponivel:
                print(f"- {veiculo}")