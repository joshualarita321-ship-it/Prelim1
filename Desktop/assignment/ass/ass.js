
let num1 = 20;
let num2 = 5;

let operator = "+";


function calculator(number1, number2, operation) {
    if (operation === "+") {
        return number1 + number2;
    } else if (operation === "-") {
        return number1 - number2;
    } else {
        
        return number1 + number2;
    }
}

console.log(calculator(num1, num2, operator));


operator = "-";

console.log(calculator(num1, num2, operator));


operator = "";

console.log(calculator(num1, num2, operator));