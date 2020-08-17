import adivinhacao
import forca

print("************************************")
print("******* Escolha seu jogo! **********")
print("************************************")

print("(1) Adivinhação - (2) Forca")
escolha = int(input("Qual jogo? "))

if(escolha == 1):
    adivinhacao.jogar()
elif(escolha == 2):
    forca.jogar()
else:
    print("Opção inválida...")
