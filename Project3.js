document.querySelector('.check-box').addEventListener('click', function (){
  const inputNumber = Number(document.querySelector('.input-box').value) ;
  console.log(randomNumber);

  if(questionText.textContent!='?')
  {

      document.body.style.background = "linear-gradient(to top right, #9198e5, #f78773, #ffaf8a)" ;
      checkBox.style.backgroundColor = "skyblue";
      checkBox.style.border = "2px solid yellow";



      scoreCounter = 10 ;
      score.textContent = 10;
      questionText.textContent = '?' ;
      inputBox.value = '';
      hintText.textContent = `Let's start Guessing...`;



      randomNumber = generateNumber();
  }

  else if(inputNumber=='' || !Number(inputNumber) || inputNumber>100 || inputNumber<1){
      hintText.textContent = `Invalid input` ;
  }

  else if(checkNum(inputNumber,randomNumber)){


      hintText.textContent = `👍 Correct!`;
      if(Number(highScore.textContent)<Number(scoreCounter)){highScore.textContent = scoreCounter ; }
      questionText.textContent = inputNumber ;
      scoreCounter = 10;
      score.textContent = 10;


      questionText.style.background = 'pink';
      document.body.style.background = "linear-gradient(to top right,#4f705e,#62e39c)" ;
      checkBox.style.background = "grey";
      checkBox.style.border = "1px solid transparent" ;

  }


  else{
      hintText.textContent = getHint(inputNumber,randomNumber) ;
      scoreCounter--;

      if(lose(scoreCounter)) {
          hintText.textContent = 'You lost.......' ;
          scoreCounter = 10 ;
          score.textContent = 10;
          randomNumber = generateNumber() ;
      }


  }
  score.textContent = scoreCounter ;
}
)


document.querySelector('.reset').addEventListener('click',function(){

  document.body.style.background = "linear-gradient(to top right, #9198e5, #f78773, #ffaf8a)" ;
  checkBox.style.backgroundColor = "skyblue";
  checkBox.style.border = "2px solid yellow"


  scoreCounter = 10 ;
  score.textContent = 10;
  inputBox.value = '';
  hintText.textContent = `Let's start Guessing...`;


  randomNumber = generateNumber();

})

function generateNumber(){
  return Math.trunc(Math.random()*100) + 1 ;
}

function checkNum(inputNum,correctNum){
  if(inputNum!=correctNum){return false;}
  else{return true;}
}

function getHint(inputNum, correctNum){
  if(inputNum>correctNum){return `Too High !`;}
  else{return `Too Low !`;}
}

function lose(scoreCounter)
{
  if(scoreCounter!=0){return false;}
  else{return true;}
}
