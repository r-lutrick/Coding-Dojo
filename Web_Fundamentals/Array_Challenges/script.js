// Always Hungry
// Write a function that is given an array and each time the value is "food" it should console log "yummy".
//  If "food" was not present in the array console log "I'm hungry" once.

function alwaysHungry(arr) {
    var nf = true;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == "food") {
            console.log("yummy");
            nf = false;
        }
    }
    if (nf) {
        console.log("I'm hungry");
    }
}

// alwaysHungry([3.14, "food", "pie", true, "food"]);   // this should console log "yummy", "yummy"
// alwaysHungry([4, 1, 5, 7, 2]);                       // this should console log "I'm hungry"



// High Pass Filter
// Given an array and a value cutoff, return a new array containing only the values larger than 
// cutoff.

function highPass(arr, cutoff) {
    var filteredArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
// console.log(result);                                             // we expect back [6, 8, 10, 9]



// Better than average
// Given an array of numbers return a count of how many of the numbers are larger than the average.

function betterThanAverage(arr) {
    var sum = 0;
    // calculate the average
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    sum = sum / arr.length
    var count = 0;
    // count how many values are greated than the average
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > sum) {
            count++;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
// console.log(result);                                                         // we expect back 4



// Array Reverse
// Write a function that will reverse the values an array and return them.

function reverse(arr) {
    for (let i = 0; i < arr.length; i++) {
        var t = arr.pop()
        arr.push(arr[i])
        arr[i] = t
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);                                    // we expect back ["e", "d", "c", "b", "a"]
