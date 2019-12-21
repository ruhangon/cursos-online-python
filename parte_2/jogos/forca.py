def jogar():
    print("JOGO DA FORCA")
    palavra_secreta="banana"
    enforcou = False
    acertou=False
    
    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute=chute.strip()
        posicao=0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, posicao))
            posicao=posicao+1
        print("Jogando...")

if (__name__ == "__main__"):
    jogar()

