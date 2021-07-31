function printPart(letter)
{
    console.log(`Part ${letter}`) ;
}
function calculateTip(bill)
{
    return(bill >= 30 && bill <= 300 ? bill*.15 : bill*.2) ;
}
function getTotal(bill)
{
    let tip = calculateTip(bill) ;
    let total = bill + tip ;
    console.log(`The bill was ${bill}, the tip was ${tip}, and the total value was ${total}`);
}
printPart('A');
getTotal(275);
getTotal(40);
getTotal(430);

function convertToFahrenheit(celcius)
{
    let fahrenheit = celcius*1.8 +32 ;
    console.log(`${celcius}°C is ${fahrenheit}°F`) ;
}
function convertToCelcius(fahrenheit)
{
    let celcius = (fahrenheit-32) * (5/9) ;
    console.log(`${fahrenheit}°F is ${celcius}°C`) ;
}
printPart('B');
convertToFahrenheit(37.4) ;
convertToCelcius(32);


const calcAverage = (score1, score2, score3) => (score1+score2+score3)/3 ;
const checkWinner = (avgNets,avgKnicks) => {

    let message = `Nets: ${avgNets} Knicks: ${avgKnicks} \n ` + (avgNets/avgKnicks<2 &&     avgKnicks/avgNets<2 ? ` There's no winner.` : avgNets>avgKnicks ? `The Nets are your champions!` : `The Knicks are your Champions!`);
    console.log(message) ;

}
printPart('C');
let avgNets = calcAverage(30,30,30);
let avgKnicks = calcAverage(30,30,30);
checkWinner(avgNets,avgKnicks);

printPart('D');
function calcTip(bill)
{
    return(bill >= 50 && bill <= 300 ? bill*.15 : bill*.2) ;
}
function calcTotal(bill, tip)
{
    return bill+tip;
}
function printTotal(bill,tips,total)
{
    console.log(`Bill:${bill} Tips: ${tips} Total: ${total}`);
}
const bill = [125, 555, 44];
const tips = [];
const total = [];
let index;
for(index of bill)
{
    tips.push(calcTip(index));
}
for(index in bill)
{
    total.push(calcTotal(bill[index],tips[index]));
}

for(index in total)
{
    printTotal(bill[index],tips[index],total[index]) ;
}
