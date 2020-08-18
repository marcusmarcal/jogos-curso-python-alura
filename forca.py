def jogar():
    print("*******************************************")
    print("** Bem-vindo ao jogo de Forca do Dionei! **")
    print("*******************************************")

    palavra_secreta = "sabugo".upper()
    tamanho = len(palavra_secreta)
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print("Palavra: ", letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrou a letra {} na posição {}".format(chute, index))
                index += 1
        else:
            erros += 1
            print("Erros: {}".format(erros))
            if(erros == 6):
                enforcou = True
                print("ENFORCOU!!")
                break
        print("Palavra: ", letras_acertadas)
        print("Jogando...")


        if "_" not in letras_acertadas:
            acertou = True
            print("**************************************")
            print("PARABÉNS, A PALAVRA ERA {}".format(palavra_secreta))
            print("**************************************")

if(__name__ == "__main__"):
    jogar()