import random

def jogar():
    print("JOGO DA ADIVINHAÇÃO")
    numero_secreto=random.randrange(1, 101)
    pontos=1000
    pontos_perdidos=0
    numero_de_tentativas=0
    print(numero_secreto)

    print("Defina um nível (1. fácil - 2. médio - 3. difícil)")
    nivel=int(input("nível: "))

    if(nivel==1):
        numero_de_tentativas=20
    elif(nivel==2):
        numero_de_tentativas=10
    elif(nivel==3):
        numero_de_tentativas=5

    for rodada in range(1, numero_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))    
        chute_str = input("Digite o seu palpite (1 a 100): ")
        chute = int(chute_str)

        print("Você digitou: ", chute)

        if (chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou=chute==numero_secreto
        maior = chute>numero_secreto
        menor = chute<numero_secreto

        if (acertou):
            print("Você acertou")
            break
        elif (maior):
            print("Você errou! O número secreto está abaixo do número digitado.")
        elif (menor):
            print("Você errou! O número secreto está acima do número digitado.")
        pontos_perdidos=abs(numero_secreto-chute)
        pontos=pontos-pontos_perdidos

    print("Fim de jogo! Você fez {} pontos.".format(pontos))


if (__name__ == "__main__"):
    jogar()

