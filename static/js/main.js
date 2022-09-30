let expanded = false;

function showCheckboxes() {
  let checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

let valider = document.getElementById('valider')
let messageError = document.getElementById('messageError')

// limit slider display umber question
let nbQuestion = document.getElementById("nbQuestion");
let limit = document.getElementById("limit");

if(window.location.pathname === '/quizz/index') {

  //display limit
  nbQuestion.innerHTML = limit.value;
  limit.addEventListener("change", () => {
    nbQuestion.innerHTML = limit.value;
  })

  let option = document.getElementById('option')
  let checkName = document.getElementById('name')

  //control pseudo empty onSubmit
  valider.addEventListener('click', (e) => {
    e.preventDefault()
    if(checkName.value === ""){
      messageError.innerHTML = 'Remplir ce champs'
    }else{
      option.submit()
    }
  })

  //control pseudo empty
  checkName.addEventListener('change', (e) => {
    if(checkName.value === ""){
      messageError.innerHTML = 'Remplir ce champs'
    }else{
      messageError.innerHTML = ''
    }
  })
}

if(window.location.pathname === '/quizz/question') {
  
  let response = document.getElementById("response");
  let proposition = document.querySelectorAll(".proposition");

  // check radio is true
  valider.addEventListener('click', (e) => {
    e.preventDefault()

    proposition.forEach((selectResponse) => {
      if(selectResponse.checked === true){
        response.submit()
      }else{
        messageError.innerHTML = 'selectionner une reponse'
      }
    })
  })
}