def exibirMensagem():
    print("ola python")

exibirMensagem() # chamar função

#recebe parametro e retprna valor
def exibirMensagemPlus(mensagem):
    print("ola python " + mensagem ) # contatenando

exibirMensagemPlus( "José") 


def multiplicar( num1, num2):
    valor = num1 * num2
    #print(valor)
    return valor
    

#print(multiplicar(4,2))
retorna = multiplicar(4,2)
print(retorna)

def bob():
    return "buuu"

print(bob())
