from jogo_velha_OO import Velha 

jogo = Velha() # importa a classe "Velha"

jogo.Desenhar() # pega o metodo da classe importada. No caso desenha o tabuleiro

# jogada humana
jogadaLinha = int(input("digite linha:"))
jogadaColuna = int(input("digite coluna:"))
jogo.lista0[jogadaLinha] [jogadaColuna] = "X" 

jogo.Desenhar()

 # Jogada da máquina
jogadaLinha = jogo.jogarMaquina()
jogadaColuna = jogo.jogarMaquina()
jogo.tabuleiro[jogadaLinha][jogadaColuna] = 'O'
print('Máquina jogou')
jogo.Desenhar()

resultado = jogo.verificarVencedor()

if resultado["X"]: # testa se é true
    print("X venceu")
elif resultado["O"]:
    print("O venceu")
else:
    print("empate")


