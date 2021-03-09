import forca
import advinhacao

def escolhe_jogo():

    print("----------------------------------")
    print("ㅤﾠﾠﾠﾠﾠﾠﾠﾠ|Escolha um jogoㅤﾠﾠﾠﾠﾠﾠﾠﾠ|")
    print("----------------------------------")

    print("1 - Advinhação | 2 - Forca")

    jogo = int(input("Digite qual dos jogos deseja jogar: "))

    if(jogo == 1):
        print("Jogando Advinhação")
        advinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()