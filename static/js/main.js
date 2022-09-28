// select option selected
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

// limit slider display umber question
let nbQuestion = document.getElementById("nbQuestion");
let limit = document.getElementById("limit");

if(window.location.pathname === '/quizz/') {
  nbQuestion.innerHTML = limit.value;

  limit.addEventListener("change", () => {
    nbQuestion.innerHTML = limit.value;
  })
}


// selected response
let proposition = document.querySelectorAll("propositon");


console.log(proposition)