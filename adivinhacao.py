print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = 45
total_tentativas = 3 #declarando o maximo de tentativas
rodada = 1 #declarando o minimo da tentativa, em qual rodada esta

while(rodada <= total_tentativas): ##laço de repetição
    #print("Tentativa", rodada,"de", total_tentativas)
    print("Tentaiva {} de {}". format(rodada, total_tentativas)) #fazendo a mesma coisa do print acima, porem "elegante"
    chute = input("Digite seu numero:")
    print("Voce digitou", chute)
    chute = int(chute)  #var chute estava como string, imput sempre retorna string, para funcionar transforma em int#

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("voce acertou!")
    else:
        if(maior):
            print("voce errou, seu numero é maior que o numero secreto!")
        elif(menor): #encadeia o if para ele nao ficar se repetindo#
            print("voce errou, seu numero é menor que o numero secreto!")

    rodada = rodada + 1


