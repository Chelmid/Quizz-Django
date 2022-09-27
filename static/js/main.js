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

let nbQuestion = document.getElementById("nbQuestion");
let limit = document.getElementById("limit");
limit.innerHTML = nbQuestion.value

nbQuestion.addEventListener("change", () => {
  limit.innerHTML = nbQuestion.value
})