def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    tamanho = len(palavra_secreta)
    # letras_acertadas = ["_", * tamanho] ## como faiz??
    letras_acertadas = ["_", "_", "_", "_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print("Encontrou a letra {} na posição {}".format(chute, index))
            index = index + 1
        print(letras_acertadas)
        print("Jogando...")

if(__name__ == "__main__"):
    jogar()