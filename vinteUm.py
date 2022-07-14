import random
import string
from turtle import clear

comecar='s';
placarJogador=0;
placarComputador=0;
empate=0;

while comecar=='s':
    
   n1= gerado = random.randint(1,11) 
   n2= gerado = random.randint(1,11)  
   n3= gerado = random.randint(1,11)  
   n4= gerado = random.randint(1,11)  
   
   somaJogador= n1+n2;
   somaBanca= n3+n4
   print("Suas cartas são: ",n1,"e",n2,"\nE a soma delas são: ",somaJogador)
   resposta = 's'
   while resposta=='s':
    resposta(str(input("Você quer mais cartas?(s/n)")))
    if resposta=='s':
        carta= gerado = random.randint(1,11)
        somaJogador+=carta
        print("A sua nova carta é: ",carta,"\nA soma é: ",somaJogador)
        if somaJogador>21:
            print("Você estourou!")
            break;
    print("As cartas da banca é: ", n3, n4,"\nA soma é: ",somaBanca)
    if somaJogador <= 21:
        while somaBanca < somaJogador and somaBanca < 21:
            carta= gerado = random.randint(1,11)
            somaBanca+=carta
            print("A nova carta da banca é: ",carta,"\nA soma é: ", somaBanca)

    if somaBanca > 21:
        placarJogador+=1
        print("A banca estourou")

    elif somaJogador > 21:
        placarComputador+=1
        print("O jogador estourou")
    elif somaJogador==somaBanca:
        empate+=1
        print("Empate")
    elif somaBanca > somaJogador:
        placarComputador+=1
        print("A banca ganhou")
    elif somaJogador > somaBanca:
        placarJogador+=1
        print("Você ganhou")

    print("====Placar====");
    print("Jogador= ",placarJogador," X ","Banca= ",placarComputador, "\nEmpate= ",empate);
    print("Você quer continuar?");
    comecar (input());
                
