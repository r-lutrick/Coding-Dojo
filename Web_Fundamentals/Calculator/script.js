var reset = true;
var a = 0;
var op = '';

function press(n) {
    if (reset == true) {
        document.querySelector('#display').innerText = n;
        reset = false;
    }
    else {
        document.querySelector('#display').innerText += n;
        reset = false;
    }
}

function clr(){
    document.querySelector('#display').innerText = 0;
    reset = true;
}

function setOP(opp) {
    a = document.querySelector('#display').innerText;
    op = opp;
    reset = true;
}

function calculate() {
    var b = document.querySelector('#display').innerText;
    a = Number(a);
    b = Number(b);
    if (op == '+') {
        var sum = a + b;
        document.querySelector('#display').innerText = sum;
        reset = true
    } else if (op == '-') {
        var sum = a - b;
        document.querySelector('#display').innerText = sum;
        reset = true;
    } else if (op == '*') {
        var sum = a * b;
        document.querySelector('#display').innerText = sum;
        reset = true;
    } else if (op == '/') {
        var sum = a / b;
        document.querySelector('#display').innerText = sum;
        reset = true;
    }
    
}
