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
const charstore = document.getElementById('charstore')

// where to append the selected characters
const selectedChars = new Set();


document.getElementById("perm_result").innerHTML = `Total number of permutations are = <strong>${permutation_data}</strong>`;
document.getElementById('n').innerHTML = `Total amount in a set ‘n’ = <strong>${n_data}</strong>`;
document.getElementById('r').innerHTML = `Amount in each subset ‘r’ = <strong>${r_data}</strong>`;

// Show the number of elements to be selected
const msg = `<span>Select ${n_data} variables from the keybord<span>`;
document.getElementById('select_char').innerHTML = msg;



let keys_row = document.getElementById('keys_row')
var clicks = 0;
const variables = "";

local_data = localStorage.setItem("variables", variables);

const createEl = (char, clicks) => {
    var card_body = document.getElementById('card_body')
    var el = document.createElement("div");
    el.classList.add("key--letter");
    selectedChars.add(char)
    if (selectedChars.size > n_data) {
        alert(`Not allowed, you can't select more than ${n_data} variables`)
        main_key.classList.add("disabledbutton")
        char = none
    }

    console.log(selectedChars)
    // el.innerHTML = `<div class="col-12"><hr><p>${clicks}. ${char}</p></div>`;
    el.innerHTML = `<div data-char="${char}">${char}</div>`

    // card_body.appendChild(el);
    document.getElementById('char_row').appendChild(el)
    

}
const nextChoices = (char) => {
    ` <div class="row mt-3">
        <div class="col-12">
            <p>Now yopu have these choices</p>
            <ul class="list-group">
                <ol class="list-group-item d-flex justify-content-between align-items-center">
                AC
                <span class="badge badge-primary badge-pill"><i class="bi bi-check"></i></span>
                </ol>
                <ol class="list-group-item d-flex justify-content-between align-items-center">
                    CA
                    <span class="badge badge-primary badge-pill"><i class="bi bi-check-circle-fill"></i></span>
                </ol>
            
            </ul>
        </div>
    
    </div>`
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
                    char: 'abc',

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
