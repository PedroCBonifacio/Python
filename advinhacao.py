
import random
import os
def jogar():

    print ("--------------------------------")
    print ("Bem vindo ao jogo de Advinhação!")
    print ("--------------------------------")

    numero_oculto = random.randrange(1, 101)
    tentativas = 0

    nivel = 0
    pontos = 1000

    print("Qual nível de dificuldade deseja jogar?")
    print("Sendo: 1 (Fácil) | 2 (Médio) | 3 (Difícil)")

    while (nivel != 1 or nivel != 2 or nivel != 3):
        nivel = int(input("Digite o nível desejado: "))
        if(nivel == 1):
            tentativas = 10
            break
        elif(nivel == 2):
            tentativas = 5
            break
        elif(nivel == 3):
            tentativas = 3
            break
        else:
            os.system("cls")
            print("Digite uma dificuldade válida (1, 2 ou 3)")
            continue

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("--------------------------------")
        print("Você digitou:",chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número apenas entre 1 e 100!")
            print("--------------------------------")
            continue

        acertou = chute == numero_oculto
        maior   = chute > numero_oculto
        menor   = chute < numero_oculto

        if(acertou):
            print("--------------------------------")
            print("Parabéns, voce acertou!")
            print("Você fez: {} pontos".format(pontos))
            break
        else:
            print("--------------------------------")
            if(maior):
                print("Você errou, o número secreto é menor.")
            elif(menor):
                print("Você errou, o número secreto é maior.")
            if (rodada == tentativas):
                print("--------------------------------")
                print("Fim de Jogo ")
                print("--------------------------------")
                print("O número secreto era: {} \n Você fez {} pontos".format(numero_oculto, pontos))


        pontos_perdidos = abs(numero_oculto - chute)
        pontos = pontos - pontos_perdidos

        print("--------------------------------")


if (__name__ == "__main__"):
    jogar()