## Testando desenvolvimento Python orientado pelo curso da Alura!
## Marcus Marçal - marcus.marcal@gmail.com
## >>> Dev <<< versão 0.1.1

import random
#import os #se necessário para função cla, lipar tela...

def jogar():
    mensagem_inicio() #Chama função da mensagem inicial do jogo
    palavra_secreta = carrega_palavra() #Chama função que carrega a palavra secreta
    letras_acertadas = carrega_letras_acertadas(palavra_secreta) #Carrega função de letras acertadas
    letras_erradas = []
    imprime_previa_palavra_secreta(letras_acertadas)

    enforcou = False
    acertou = False
    vidas = 7

    while (not acertou and not enforcou):
        chute = fazer_chute()
        if (chute in palavra_secreta):
            marca_letra_acertada(chute, letras_acertadas, palavra_secreta)
        else:
            vidas -= 1
            marca_letra_errada(chute, letras_erradas, vidas)
            desenha_forca(vidas)

            if (vidas == 0):
                enforcou = True
                imprime_mensagem_perdedor(palavra_secreta)
                escolher_jogar_de_novo()
                
        imprime_mensagem_jogando(letras_acertadas, letras_erradas, vidas)

        if "_" not in letras_acertadas:
            acertou = True
            imprime_mensagem_vencedor(palavra_secreta)
            escolher_jogar_de_novo()

def mensagem_inicio():
    print("*******************************************")
    print("** Bem-vindo ao jogo de Forca do Marcus! **")
    print("*******************************************")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    tamanho = len(palavras)
    escolhida = palavras[random.randrange(0, tamanho)].upper()
    arquivo.close()
    return escolhida

def carrega_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def fazer_chute():
    chute = input("Qual letra? ")
    return chute.strip().upper()

def marca_letra_acertada(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            # print("Encontrou a letra {} na posição {}".format(chute, index))
        index += 1

def imprime_previa_palavra_secreta(lista):
    print("Palavra SECRETA: ", lista)

def imprime_mensagem_jogando(letras_acertadas, letras_erradas, erros):
    if letras_erradas:
        print("Letras erradas: {}".format(letras_erradas))
    # print("Erros disponíveis: {}".format(erros))
    print("PALAVRA SECRETA: ", letras_acertadas)

def marca_letra_errada(chute, letras_erradas, erros):
    letras_erradas.append(chute)

def imprime_mensagem_perdedor(palavra_secreta):
    print("****************** ENFORCOU!! ******************")
    print("***** A PALAVRA ERA >>> {} <<< *****".format(palavra_secreta))
    print("************************************************\n")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor(palavra_secreta):
    print("******************* PARABÉNS *******************")
    print("A PALAVRA ERA >>> {} <<<".format(palavra_secreta))
    print("************************************************")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def escolher_jogar_de_novo():
    novo = input("Jogar de novo? [S] ou [N] ").upper()
    if novo == "S":
        jogar()
    else:
        print("************* ATÉ A PRÓXIMA! **************")
    exit()

def desenha_forca(vidas):
    print("  _______     ")
    print(" |/      |    ")

    if(vidas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(vidas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(vidas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(vidas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(vidas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(vidas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (vidas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
