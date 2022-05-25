import random
jogador = 0
computador = 0
escolha = 0

while escolha !=0:
    print("Escolha: \n1–Ímpar \n2–Par \n0–Sair")
    escolha=input()
    if escolha == 0:
        exit()
    gerado = random.randint(0,100)
    if escolha == 1 & gerado%2==0:
        computador+=1
        print("Você escolheu Impar, e o número",gerado,"é Par.\nVocê errou!")
        print("------Placar------")
        print("Jogador -",jogador,"\nComputador -",computador)
    elif escolha == 1 & gerado%2!=0:
        jogador+=1
        print("Você escolheu Impar, e o número",gerado,"é Ímpar.\nVocê acertou!")
        print("------Placar------")
        print("Jogador -",jogador,"\nComputador -",computador)
    elif escolha == 2 & gerado%2==0:
        jogador+=1
        print("Você escolheu Par, e o número",gerado,"é Par.\nVocê acertou!")
        print("------Placar------")
        print("Jogador -",jogador,"\nComputador -",computador)
    elif escolha == 2 & gerado%2!=0:
        computador+=1
        print("Você escolheu Par, e o número",gerado,"é Ímpar.\nVocê errou!")
        print("------Placar------")
        print("Jogador -",jogador,"\nComputador -",computador)
    else:
        print("Você informou algo diferente de 0, 1 e 2!!")
