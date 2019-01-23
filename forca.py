def jogar():
    print("*********************************")
    print("Bem Vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

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
                index = index + 1
            print(letras_acertadas)
        else:
            erros = erros + 1

            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)
    if(acertou):
        print("Voce Ganhou!")
    else
        print("Voce perdeu")

    print("Fim do Jogo")

if(__name__== "__main__"):
    jogar()