// Brute FORCE
// for (var i=1; i<=100; i++){
//     if (i % 3 != 0 && i % 5 != 0){
//         console.log(i)
//     }
//     else {
//         if (i % 3 != 0 && i % 5 == 0){
//             console.log("Buzz")
//         }
//         else {
//             if (i % 3 == 0 && i % 5 != 0){
//                 console.log("Fizz")
//             }
//             else {console.log("FizzBuzz")}
//         }
//     }
// }

// Version 2
for (var i=1; i<=100; i++){
    // var out = ((i%3!=0) && i) || "Fizz" // Version2.1 (fail)
    // var out = ( ((i%3==0) && "Fizz") + ((i%5==0) && "Buzz") ) || i // Version 2.2 (fail)
    var out = (i%3!==0 && i%5!==0) && i || (i%3==0 && i%5==0) && "FizzBuzz" || (i%3!==0) && "Buzz" || "Fizz" // Version 2.3
    console.log(out);
}