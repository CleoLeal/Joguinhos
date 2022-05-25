import random
from turtle import clear
jogador = 0
computador = 0
escolha = -1

while escolha != 0:
    escolha = int(input("Escolha: \n1–Ímpar \n2–Par \n0–Sair"))
    if escolha == 0:
        exit()
    gerado = random.randint(0, 100)
    if escolha == 1 and (gerado % 2) == 0:
        computador += 1
        print("Você escolheu Ímpar, e o número", gerado, "é Par. Você errou!")
        print("------Placar------")
        print("Jogador -", jogador, "\nComputador -", computador)
    elif escolha == 1 and (gerado % 2) != 0:
        jogador += 1
        print("Você escolheu Ímpar, e o número", gerado, "é Ímpar. Você Acertou!")
        print("------Placar------")
        print("Jogador -", jogador, "\nComputador -", computador)
    elif escolha == 2 and (gerado % 2) == 0:
        jogador += 1
        print("Você escolheu Par, e o número", gerado, "é Par. Você acertou!")
        print("------Placar------")
        print("Jogador -", jogador, "\nComputador -", computador)
    elif escolha == 2 and (gerado % 2) != 0:
        computador += 1
        print("Você escolheu Par, e o número", gerado, "é Ímpar. Você errou!")
        print("------Placar------")
        print("Jogador -", jogador, "\nComputador -", computador)

    escolha = input()
