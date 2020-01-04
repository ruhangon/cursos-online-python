import random

def jogar():
    print("JOGO DA FORCA")

    palavra_secreta=carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou=False
    tentativas=0
    
    print(letras_acertadas)
    
    while(not acertou and not enforcou):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas=tentativas+1
        print(letras_acertadas)
        enforcou = tentativas == 10
        acertou = "_" not in letras_acertadas

    if (acertou):
        print("Você ganhou! Parabéns!")
    else:
        print("Você perdeu.")
        print("A palavra era {}".format(palavra_secreta))

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip()
    chute=chute.lower()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

if (__name__ == "__main__"):
    jogar()

