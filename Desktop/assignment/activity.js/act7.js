 addTwoNumber = (x , y) => x + y;
let resultsArr = []; 

for(let i = 0; i < 10; i ++){
    let result = addTwoNumber(i, 2*i); 
    resultsArr.push(result);
}
console.log(resultsArr);