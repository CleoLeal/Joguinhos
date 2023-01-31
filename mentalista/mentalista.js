//this serves to get the data from the console
const enter = require('prompt-sync')({sigint:true});
//Ramdom number variable
var secretNumber = parseInt(Math.random()*1001);
//char variable
var start = 'y';
var computer =0, player=0;
//while "start" equaly to 'y' (yes)
while(start=='y')
{
    //do..
    do{
        //show on console and get the data with luck variable
        var luck = enter("Guess a number from 1 to 100");
        //if luck equal to secretNumber
        if(luck == secretNumber)
        {
            //player wins one point
            player++;
            //so show on console this text
            console.log("Congratulations. You got ir right!");
        }
        //else if luck is greater secreteNumber
        else if(luck > secretNumber)
        {
            //computer wins one point
            computer++;
            //so show on console this text
            console.log("You missed. The number is less.");
        }
        //else if luck is lower secreteNumber
        else if(luck < secretNumber)
        { 
            //player wins one point
            computer++;
            //so show on console this text
            console.log("You missed. The number is bigger.");
        }
    //...while luck is different from secretNumber     
    }while(luck!=secretNumber)
    //this it is the scoreboard
    console.log("===Scoreboard===");
    //the sum
    console.log("Computer= "+ computer +"\nPlayer= " + player);
    //the question...to begin with
    start=enter("Do you want to continue?(y/n)");
}


  
   