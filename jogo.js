//essa é uma biblioteca para conseguir adquirir os dados digitados no console
//npm i prompt-stnc
const enter = require('prompt-sync')({sigint: true});
var secretNumber=parseInt(Math.random()*1001);

var start = 'y';
var computer = 0, player =0;
while (start == 'y')
{
    var question = 'y';
    while (question == 'y')
    {
        question= enter("Let's start?(y/n)");
        if (question == 'y')
        {
            while(luck!=secretNumber)
            {
                var luck = enter("Guess a number from 1 to 1000");
                if(luck==secretNumber)
                {
                    player ++;
                    console.log("Congratulations. You got it right");
                }
                else if(luck > secretNumber)
                {
                    computer ++;
                    console.log("You missed. The number is less");
                }
                else if(luck < secretNumber)
                {
                    computer ++;
                    console.log("You missed. The number is bigger");
                }
            }
            
        }
    }
        Console.WriteLine("====Placar====");
        Console.WriteLine("Computer= " + computer + " X " + "Player= " + player);
        start= enter("Do you want to continue?(y/n)");
}