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

let keys = document.querySelectorAll('.key--letter');


const safeEl = []

const n_data = localStorage.getItem("n");
const r_data = localStorage.getItem("r");
const permutation_data = localStorage.getItem("result");


document.getElementById("perm_result").innerHTML = `Total number of permutations are = <strong>${permutation_data}</strong>`;
document.getElementById('n').innerHTML = `Total amount in a set ‘n’ = <strong>${n_data}</strong>`;
document.getElementById('r').innerHTML = `Amount in each subset ‘r’ = <strong>${r_data}</strong>`;


let keys_row = document.getElementById('keys_row')
var clicks = 0;
const variables = "";

local_data = localStorage.setItem("variables", variables);

const createEl = (char, clicks) => {
    var card_body = document.getElementById('card_body')

    var el = document.createElement("div");
    el.classList.add("row");
    el.classList.add("mt-3");

    el.innerHTML = `<div class="col-12"><hr><p>${clicks}. ${char}</p></div>`;
    card_body.appendChild(el);

}


for (var x = 0; x < keys.length; x++) {
    keys[x].onclick = function(){
        clicks += 1;
        
        let char = this.getAttribute('data-char')
        createEl(char, clicks)

        localStorage.setItem("variable", char);
    
        fetch('/calculator/get-permutation', {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body: JSON.stringify({
                payload:{
                    char: 'ac',

                }
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.data)


        })
        .catch((error) => {

        })
    }
};
