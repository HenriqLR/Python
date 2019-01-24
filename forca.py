import random
def jogar():
    print("*********************************")
    print("Bem Vindo ao jogo de Forca!")
    print("*********************************")

    arquivo = open("palavra.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    erros    = 0

    print(letras_acertadas)

    #Enquanto{ True )
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra):
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Voce Ganhou!")
    else:
        print("Voce perdeu")

    print("Fim do Jogo")

if(__name__== "__main__"):
    jogar()