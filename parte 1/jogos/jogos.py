import forca
import adivinhacao

def escolhe_jogo():
    print("Escolha um jogo")
    print("1. Jogo da forca - 2. Jogo da adivinhação")
    jogo=int(input("Qual o jogo: "))

    if (jogo==1):
        print("Você escolheu o jogo da forca")
        forca.jogar()
    elif (jogo==2):
        print("Você escolheu o jogo da adivinhação")
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()

    