def jogar():
    print("JOGO DA FORCA")
    palavra_secreta="banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou=False
    
    print(letras_acertadas)
    
    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute=chute.strip()
        posicao=0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                letras_acertadas[posicao] = letra
            posicao=posicao+1
        print(letras_acertadas)

if (__name__ == "__main__"):
    jogar()

