let expanded = false;

function showThemes() {
  let checkboxesThemes = document.getElementById("checkboxesThemes");
  if (!expanded) {
    checkboxesThemes.style.display = "block";
    expanded = true;
  } else {
    checkboxesThemes.style.display = "none";
    expanded = false;
  }
}

function showLevel() {
  let checkboxesLevel = document.getElementById("checkboxesLevel");
  if (checkboxesLevel.style.display === "block") {
    checkboxesLevel.style.display = "none";
  } else {
    checkboxesLevel.style.display = "block";
  }
}

let valider = document.getElementById('valider');
let messageError = document.getElementById('messageError');

// limit slider display umber question
let nbQuestion = document.getElementById("nbQuestion");
let limit = document.getElementById("limit");

if(window.location.pathname === '/quizz/index') {

  //display limit
  nbQuestion.innerHTML = limit.value;
  limit.addEventListener("change", () => {
    nbQuestion.innerHTML = limit.value;
  })

  let option = document.getElementById('option');
  let checkName = document.getElementById('name');

  //control pseudo empty onSubmit
  valider.addEventListener('click', (e) => {
    e.preventDefault();
    if(checkName.value === ""){
      messageError.innerHTML = 'Remplir ce champs';
    }else{
      option.submit();
    }
  })

  //control pseudo empty
  checkName.addEventListener('change', (e) => {
    if(checkName.value === ""){
      messageError.innerHTML = 'Remplir ce champs';
    }else{
      messageError.innerHTML = '';
    }
  })
}

if(window.location.pathname === '/quizz/question') {
  
  let response = document.getElementById("response");
  let proposition = document.querySelectorAll(".proposition");

  // remove error if not empty
  //bug
  // response.addEventListener('change', (e) => {
  //   if(e.target.checked === true){
  //     messageError.innerHTML = "";
  //   }
  // })

  // check radio is true
  valider.addEventListener('click', (e) => {
    e.preventDefault();

    proposition.forEach((selectResponse) => {

      if(selectResponse.checked === false){
          messageError.innerHTML = 'Selectionner une reponse';
      }else{
        messageError.innerHTML =  "";
        response.submit();
      }
    })
  })
}