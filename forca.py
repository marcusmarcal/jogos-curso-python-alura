## Testando desenvolvimento Python orientado pelo curso da Alura!
## Marcus Marçal - marcus.marcal@gmail.com

import random
#import os #se necessário para função cla, lipar tela...

def jogar():
    mensagem_inicio() #Chama função da mensagem inicial do jogo

    palavra_secreta = carrega_palavra() #Chama função que carrega a palavra secreta

    letras_acertadas = carrega_letras_acertadas(palavra_secreta) #Carrega função de letras acertadas

    letras_erradas = []

    enforcou = False
    acertou = False
    erros = 10

    print("Palavra incompleta: ", letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrou a letra {} na posição {}".format(chute, index))
                index += 1
        else:
            erros -= 1
            letras_erradas.append(chute)

            if (erros == 0):
                enforcou = True
                print("****************** ENFORCOU!! ******************")
                print("***** A PALAVRA ERA >>> {} <<< *****".format(palavra_secreta))
                print("************************************************\n")
                novo = input("Jogar de novo? [S] ou [N] ").upper()
                if novo == "S":
                    jogar()
                else:
                    print("************* ATÉ A PRÓXIMA! **************")
                    break
        #print('\n' * 100)
        #os.system('cls')
        print("Letras erradas: {}".format(letras_erradas))
        print("Erros disponíveis: {}".format(erros))
        print("PALAVRA SECRETA: ", letras_acertadas)
        # print("Jogando...")

        if "_" not in letras_acertadas:
            acertou = True
            print("******************* PARABÉNS *******************")
            print("A PALAVRA ERA >>> {} <<<".format(palavra_secreta))
            print("************************************************")
            novo = input("Jogar de novo? [S] ou [N] ").upper()
            if novo == "S":
                jogar()
            else:
                print("************* ATÉ A PRÓXIMA! **************")
                break


def mensagem_inicio():
    print("*******************************************")
    print("** Bem-vindo ao jogo de Forca do Dionei! **")
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
    #palavra_secreta = unidecode(escolhida.upper())
    return escolhida

def carrega_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if (__name__ == "__main__"):
    jogar()
