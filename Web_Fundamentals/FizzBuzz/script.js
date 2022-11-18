// Version 1: Brute FORCE
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
// for (var i = 1; i <= 100; i++) {
//     var out =
//         (i % 3 != 0 && i % 5 != 0 && i) ||
//         (i % 3 == 0 && i % 5 == 0 && "FizzBuzz") ||
//         (i % 3 !== 0 && "Buzz") ||
//         "Fizz"; // Version 2.3
//     console.log(out);
// }

// Version 3: Optimization based on frequency.
// Intigers happen the most, fizz & buzz second most & fizzbuzz happening least frequently
for (var i = 1; i <= 100; i++) {
    var out =
        (i % 3 != 0 && i % 5 != 0 && i) || // if i is not divisible by 3 & 5, then output i (2)
        (i % 3 == 0 && i % 5 != 0 && "Fizz") || // if i is divisible by 3 & not 5, output Fizz (1)
        (i % 3 != 0 && i % 5 == 0 && "Buzz") || // i is divisible by 5 & not 3, output Buzz (1)
        "FizzBuzz"; // only option left is FizzBuzz (0)
    console.log(out);
}
