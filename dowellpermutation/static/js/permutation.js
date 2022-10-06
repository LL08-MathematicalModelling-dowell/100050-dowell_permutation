// Variable declaration

let keys = document.querySelectorAll('.key--letter');
const n_data = localStorage.getItem("n");
const r_data = localStorage.getItem("r");
const permutation_data = localStorage.getItem("result");
const charstore = document.getElementById('charstore')

// where to append the selected characters
const selectedChars = new Set();
const variable = new Set();
const combination_set = new Set();

// const variable = new Set(['a', 'b', 'c']);



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

document.getElementById("perm_result").innerHTML = `Total number of permutations are = <strong>${permutation_data}</strong>`;
document.getElementById('n').innerHTML = `Total amount in a set ‘n’ = <strong>${n_data}</strong>`;
document.getElementById('r').innerHTML = `Amount in each subset ‘r’ = <strong>${r_data}</strong>`;

// Show the number of elements to be selected
const msg = `<span>Select ${n_data} variables from the keybord<span>`;
const msg_con = document.getElementById('select_char')
msg_con.innerHTML = msg;


let keys_row = document.getElementById('keys_row')

// const getSelectedchar = (char) => {
//     const selectedChars = new Set()
//     selectedChars.add(char)

//     return selectedChars
// }

// Permutation function

const do_permutation = (variables, combination_set) => {
    fetch('/calculator/get-permutation', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie("csrftoken"),
        },
        body: JSON.stringify({
            payload:{
                char: variables,

            }
        })
    })
    .then(response => response.json())
    .then(data => {
        data = data.data
        appendData(data)
        console.log(data[i])
        console.log(appendChild.data)

        // combination_set.add(str(data.data))
        // console.log('Combination', combination_set)
        
        // console.log('Combination', setResult(data.data, combination_set))

        // data.data.forEach(variable => {



        //     const markup = `<div class="form-check">
        //     <input type="radio" class="form-check-input" id="radio1" name="optradio" value="option1">${data.data}
        //     <label class="form-check-label" for="radio1"></label>
        //   </div>`
        //   document.getElementById("perm_result_con").innerHTML = markup
        // });
        // let data = data.data
        console.log('SERVER', data)
        // res = data.data
        
    })
    .catch((error) => {

    })
}

const appendData = (data) => {
    var mainContainer = document.getElementById('perm_result_con')
    for (let i = 0; i < data.length; i++) {
    //   console.log(data[i])
      var div = document.createElement("div")
      div.innerHTML = `<div class="form-check" style="display:inline">
        <input type="radio" class="form-check-input" id="radio1" name="optradio" value="option1">${data[i]}
      <label class="form-check-label" for="radio1"></label>
     </div>`
      mainContainer.appendChild(div)
    

    }
}

const removeEl = (el) => {
    el.remove();
}

const setResult = (combination_set, res) => {
    combination_set.add(data.data)
    return combination_set
}


const createEl = (char) => {
    var card_body = document.getElementById('card_body')
    var el = document.createElement("div");
    el.classList.add("key--letter");
    selectedChars.add(char)
    if (selectedChars.size > n_data) {
        alert(`Not allowed, you can't select more than ${n_data} variables`)
        main_key.classList.add("disabledbutton")
        char = none
        // msg_con.innerHTML = ''
        // document.getElementById('instruction_con').innerHTML = 'select 1ST variable from above'

    }

    // console.log('selected', selectedChars)
 
    el.innerHTML = `<div data-char="${char}">${char}</div>`

    document.getElementById('char_row').appendChild(el)
    el.onclick = function(el) {
        // console.log('Element clicked', char)

        variable.add(char)
        const variables = Array.from(variable).join('');
        // console.log('Variables', variables)

        do_permutation(variables)
        // removeEl(el)
        this.classList.add("disabledbutton")
    }
    

}



for (var x = 0; x < keys.length; x++) {
    keys[x].onclick = function(){

        let char = this.getAttribute('data-char')
    
        createEl(char)
        // do_permutation(char)
        
        
    }
};
