

const n_data = localStorage.getItem("n");
const r_data = localStorage.getItem("r");
const permutation_data = localStorage.getItem("result");


document.getElementById("perm_result").innerHTML = `Total number of permutations are = <strong>${permutation_data}</strong>`;
document.getElementById('n').innerHTML = `Total amount in a set ‘n’ = <strong>${n_data}</strong>`;
document.getElementById('r').innerHTML = `Amount in each subset ‘r’ = <strong>${r_data}</strong>`;

let keys_data = []
let keys_row = document.getElementById('keys_row')
var clicks = 0;

// function onClick() {
//   clicks += 1;
//   document.getElementById("clicks").innerHTML = clicks;
// };
// let csrf = document.getElementsByName('csrf')
// console.log(csrf.getAttribute('data-char'))

// CSRF TOKEN
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begin with the name we want
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               
                break;
            }
        }
    }

    return cookieValue;
}

const createEl = (char, clicks) => {
    var card_body = document.getElementById('card_body')

    var el = document.createElement("div");
    el.classList.add("row");
    el.classList.add("mt-3");

    el.innerHTML = `<div class="col-12"><hr><p>${clicks}. ${char}</p></div>`;
    card_body.appendChild(el);
    console.log(el)
}


let keys = document.querySelectorAll('.key--letter');
for (var x = 0; x < keys.length; x++) {
    keys[x].onclick = function(){
    clicks += 1;

    // console.log(this.getAttribute('data-char'))
    let char = this.getAttribute('data-char')
    createEl(char, clicks)
    fetch('/calculator/get-permutation', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken"),

        },
        body: JSON.stringify({
            payload:{
                char:char
            }
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)

    })
    .catch((error) => {

    })

   
  }
};
  



// class="" data-char="A"