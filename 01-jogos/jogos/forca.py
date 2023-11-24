import random

def imprime_mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta()->list:
    arquivo = open("palavras.txt", "r")
    palavras_secretas = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras_secretas.append(linha.strip())


    palavra_index = random.randint(0,len(palavras_secretas)-1)
    return palavras_secretas[palavra_index]

def inicializa_letras_acertadas(palavra):
    return len(palavra)*["_"]

def pede_chute():
    chute = input("Qual a letra? ").lower().strip()
    return chute

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    imprime_mensagem_inicial()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros_restantes = 7
    
    while(not(enforcou or acertou)):
        print("Jogando...")
        print("Numero de tentativas restantes: {}".format(erros_restantes))
        chute = pede_chute()

        index = 0
        tentativa_errada = True
        for letra in palavra_secreta:
            if(chute == letra):
                print(f'Achou a letra {chute} na posicao {index}')
                letras_acertadas[index] = chute
                tentativa_errada = False
            index+=1
        
        if(tentativa_errada):
            print("Letra {} nao encontrada, tente novamente.".format(chute))
            erros_restantes-=1

        for letra in letras_acertadas:
            print(letra, end=' ')

        print('\n')

        desenha_forca(erros_restantes)

        acertou = "_" not in letras_acertadas
        if(acertou):
            imprime_mensagem_vencedor()

        enforcou = erros_restantes == 0
        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
