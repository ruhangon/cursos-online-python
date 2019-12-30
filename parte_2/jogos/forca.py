def jogar():
    print("JOGO DA FORCA")
    palavra_secreta="banana"
    palavra_secreta=palavra_secreta.lower()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou=False
    tentativas=0
    
    print(letras_acertadas)
    
    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute=chute.strip()
        chute=chute.lower()

        if (chute in palavra_secreta):
            posicao=0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao=posicao+1
        else:
            tentativas=tentativas+1
        print(letras_acertadas)
        enforcou = tentativas == 10
        acertou = "_" not in letras_acertadas

    if (acertou):
        print("Você ganhou! Parabéns!")
    else:
        print("Você perdeu.")

if (__name__ == "__main__"):
    jogar()

