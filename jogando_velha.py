from jogo_velha_OO import Velha

jogo = Velha() # importa a classe "Velha"

jogo.Desenhar() # pega o metodo da classe importada. No caso desenha o tabuleiro

# jogada humana
jogadaLinha = int(input("digite linha:"))
jogadaColuna = int(input("digite coluna:"))
jogo.lista0[jogadaLinha] [jogadaColuna] = "X" 

jogo.Desenhar()

# jogada maquinha
#jogadaLinha = jogo.maquina()
#jogadaColuna = jogo.maquina()
#jogo.lista0[jogadaLinha] [jogadaColuna] = "O" 
