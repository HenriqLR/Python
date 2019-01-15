import random

def jogar():

    print("*********************************")
    print("Bem Vindo ao jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina um nivel:"))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel ==2):
        total_tentativas = 10
    elif(nivel ==3):
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)

        print("Voce digitou ", chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Voce Errou! O Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Voce Errou! O Seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

if(__name__== "__main__"):
    jogar()