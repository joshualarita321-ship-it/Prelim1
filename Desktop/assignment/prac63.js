let number1 = 20;
let number2 = 5;

let operator = "+"; // Change to "-" to subtract

function calculator(num1, num2, op) {

    if (op == "-") {
        return num1 - num2;
    } else {
        return num1 + num2;
    }

}

console.log("Answer: " + calculator(number1, number2, operator));


operator = "-";

console.log("Answer: " + calculator(number1, number2, operator));