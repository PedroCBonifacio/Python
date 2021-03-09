import random

def jogar():

    mensagem_abertura()
    palavra_oculta = puxar_palavra_oculta()
    letras_acertadas = espacos_letras_acertadas(palavra_oculta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativa = 0

    while(not enforcou and not acertou):

        chute = pedir_chute()

        if (chute in palavra_oculta):
            posicionar_chute_correto(chute, letras_acertadas, palavra_oculta)
        else:
            print("Você errou, agora você tem mais {} tentativas".format(6 - tentativa))
            desenho_forca(tentativa)
            tentativa += 1

        enforcou = tentativa == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mensagem_vencedora()
    else:
        mensagem_perdedora(palavra_oculta)



def mensagem_abertura():
    print("--------------------------------")
    print("ㅤﾠBem vindo ao jogo da forca!ㅤﾠ")
    print("--------------------------------")

def puxar_palavra_oculta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    posicao_palavra = random.randrange(0,len(palavras))
    palavra_oculta = palavras[posicao_palavra].upper()
    return palavra_oculta

def espacos_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pedir_chute():
    chute = input("Digite uma letra : ")
    chute = chute.strip().upper()
    return chute

def posicionar_chute_correto(chute, letras_acertadas, palavra_oculta):
    posicao = 0
    for letra in palavra_oculta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def desenho_forca(tentativa):
        print("  _______     ")
        print(" |/      |    ")

        if (tentativa == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (tentativa == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (tentativa == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (tentativa == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

def mensagem_vencedora():
    print("--------------------------------")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedora(palavra_oculta):
    print("--------------------------------")
    print("Fim de jogo, você enforcou!")
    print("A palavra era {}".format(palavra_oculta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()