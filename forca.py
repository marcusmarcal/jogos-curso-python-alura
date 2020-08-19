## Testando desenvolvimento Python orientado pelo curso da Alura!
## Marcus Marçal - marcus.marcal@gmail.com
## Versão 0.1.0

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
    erros = 10

    while (not acertou and not enforcou):
        chute = fazer_chute()
        if (chute in palavra_secreta):
            marca_letra_acertada(chute, letras_acertadas, palavra_secreta)
        else:
            erros -= 1
            marca_letra_errada(chute, letras_erradas, erros)
            
            if (erros == 0):
                enforcou = True
                imprime_mensagem_enforcou(palavra_secreta)
                escolhe_jogar_de_novo()
                
        imprime_mensagem_jogando(letras_acertadas, letras_erradas, erros)

        if "_" not in letras_acertadas:
            acertou = True
            imprime_mensagem_acertou(palavra_secreta)
            escolhe_jogar_de_novo()

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
    #palavra_secreta = unidecode(escolhida.upper())
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
            print("Encontrou a letra {} na posição {}".format(chute, index))
        index += 1

def imprime_previa_palavra_secreta(lista):
    print("Palavra SECRETA: ", lista)

def imprime_mensagem_jogando(letras_acertadas, letras_erradas, erros):
    # print('\n' * 100)
    # os.system('cls')
    print("Letras erradas: {}".format(letras_erradas))
    print("Erros disponíveis: {}".format(erros))
    print("PALAVRA SECRETA: ", letras_acertadas)

def marca_letra_errada(chute, letras_erradas, erros):
    letras_erradas.append(chute)

def imprime_mensagem_enforcou(palavra_secreta):
    print("****************** ENFORCOU!! ******************")
    print("***** A PALAVRA ERA >>> {} <<< *****".format(palavra_secreta))
    print("************************************************\n")

def escolhe_jogar_de_novo():
    novo = input("Jogar de novo? [S] ou [N] ").upper()
    if novo == "S":
        jogar()
    else:
        print("************* ATÉ A PRÓXIMA! **************")
    exit()

def imprime_mensagem_acertou(palavra_secreta):
    print("******************* PARABÉNS *******************")
    print("A PALAVRA ERA >>> {} <<<".format(palavra_secreta))
    print("************************************************")

if (__name__ == "__main__"):
    jogar()
