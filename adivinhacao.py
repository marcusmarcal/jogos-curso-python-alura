import random

print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Escolha o nível:")
print("(1) Fácil - (2) Médio - (3) Difícil")
nivel = int(input("Nível escolhido: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acertou = (chute == numero_secreto)
    maior   = (chute > numero_secreto)
    menor   = (chute < numero_secreto)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    if(acertou):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Você acertou! - PARABÉNS! - Ganhou {} pontos!".format(pontos))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi MAIOR que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi MENOR que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("*********************************")
print("Fim do jogo! Número secreto: {}".format(numero_secreto))
print("*********************************")