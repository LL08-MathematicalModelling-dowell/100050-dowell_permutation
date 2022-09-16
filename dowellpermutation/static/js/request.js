

const n_data = document.getElementById("n_data")
const r_data = document.getElementById("r_data")
const perm_form = document.getElementById('perm_form')

// containers
let no_permutation = document.getElementById('no_permutation')
let show_permutation = document.getElementById('show_permutation')
let calculate_permutation = document.getElementById('calculate_permutation')

let submit_btn = document.getElementById('submit_btn')


no_permutation.style.display = "none"



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

// const getResult = () => {

// }


const calculatePerm = (e) => {
    e.preventDefault()
    let result = 0
    submit_btn.style.display="none"

    fetch('/calculator/permutations/', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken"),
        }, 

        body: JSON.stringify({
            payload: {
                n:n_data.value,
                r:r_data.value,
            }
        })

    })
    .then(response => response.json())
    .then(data => {
        // populate the permutation result here
        console.log(data.instance['instance'])
        document.getElementById('permutation_result').innerHTML = data.instance
    })
    .catch((error) => {
        // error handling here
        console.error('Error:', error);
    })
}

perm_form.addEventListener('submit', calculatePerm)

// document.getElementById("perm_form").addEventListener("submit", function(event) {
//    event.preventDefault() 
// })






