/* Predict 1: What will console.log state when this function is called? */

function myBirthYearFunc(){
        console.log("I was born in " + 1980);
    }

// I was born in 1980



/* Predict 2: If we needed to send a birth year to the function, we would tell the function 
"hey, we're gonna send you a variable called birthYearInput." We do that by adding the variable 
name into the parentheses. See below for an example. 

So, if the variable birthYearInput is 1980 (aka var birthYearInput = 1980), and this function is 
called, what would the console.log state? */

function myBirthYearFunc(birthYearInput){
        console.log("I was born in " + birthYearInput);
    }
    
// I was born in 1980



/* Predict 3: Let's try it again. If var num1 = 10 and var num2 = 20, what would the console.log state? */

function add(num1, num2){
        console.log("Summing Numbers!");
        console.log("num1 is: " + num1);
        console.log("num2 is: " + num2);
        var sum = num1 + num2;
        console.log(sum);
    }
    
// Summing Numbers!
// num1 is: 10
// num2 is: 20
// 30
