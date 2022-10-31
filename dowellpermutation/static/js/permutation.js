// Variable declarationvar
var msg = null

let keys = document.querySelectorAll('.key--letter');
const n_data = localStorage.getItem("n");
const r_data = localStorage.getItem("r");
const permutation_data = localStorage.getItem("result");
const charstore = document.getElementById('charstore')

// where to append the selected characters
const selectedChars = new Set();
const variable = new Set();
const combination_set = new Set();


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

// // Show the number of elements to be selected
// const msg = `<span>Select ${n_data} variables from the keybord<span>`;
const msg_con = document.getElementById('select_char')
msg_con.innerHTML = msg;


// Instatiate keys 
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
       console.log(data)
        appendData(data)
        
    })
    .catch((error) => {
        console.log(error)
    })
}

// create a helper function
const setAttributes = (el, attrs) => {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
}

const appendData = (data) => {
    const variable = new Set();
    var show_d = document.getElementById("show")
    let text = ""
    // for (let i = 0; i < data.data.length; i++) { 

    //     // text += cars[i] + "<br>";
    //     console.log(data.data[i])
        
    //     //if only one data is returned
    //     if (data.data.length == 1) {
    //         //create span element and append to the show
           
    //         var span = document.createElement("span");
    //         span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${data.data[i]}">${data.data[i]}</div> `
    //         show_d.appendChild(span)
    //         span.addEventListener('click', function(params) {
    //             do_permutation(data.data[i])
    //         })
    //     }
    //     else {
            
    //         for (let i = 0; i < data.data.length; i++) {
    //             var span = document.createElement("span");
    //             span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${data.data[i]}">${data.data[i]}</div> `
    //             show_d.appendChild(span)
    //             //add event listener to the span
    //             span.addEventListener('click', function(params) {
    //                 do_permutation(data.data[i])
    //             })
    //         }

    //     }
     
      

    // }


    //append data to show_d
    // data.data.forEach(element => {
    //     var span = document.createElement("span");
    //     span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${element}">${element}</div> `
    //     //clear the show_d
    //     show_d.innerHTML = ""
    //     show_d.appendChild(span)        
    //     span.addEventListener('click', function(params) {
    //         do_permutation(element)
    //     })   
    // });
    show_d.innerHTML = ""
    for (let i = 0; i < data.data.length; i++) {
        
       if (data.data.length == 1) {
        console.log("one")
           var span = document.createElement("span");
           span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${data.data[i]}">${data.data[i]}</div> `
          
           show_d.appendChild(span)
        //    span.addEventListener('click', function(params) {
        //        do_permutation(data.data[i])
        //    })
       }
    else{
        console.log("else called")
        var span = document.createElement("span");
        span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${data.data[i]}">${data.data[i]}</div> `
        
        show_d.appendChild(span)
        // span.addEventListener('click', function(params) {
        //     do_permutation(data.data[i])
        // })
        //add event listener to select current span
        span.addEventListener('click', function(params) {
            //select the current span
            const current_span = params.target
            //get the data-char
            const current_char = current_span.getAttribute('data-char')
            console.log(current_char)
            replace_span(current_char)
        })
    }  
    }
}

function replace_span(current_char) {
    //get the show_d
    const show_d = document.getElementById('show')
    show_d.innerHTML = ""
    //create a new span
    var span = document.createElement("span");
    span.innerHTML = `<div class="key--letter btn btn-primary mt-1" data-char="${current_char}">${current_char}</div> `
    show_d.appendChild(span)
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
        msg = `Not allowed, you can't select more than ${n_data} variables`
        warningModal('Invalid Input', msg)
        // alert(`Not allowed, you can't select more than ${n_data} variables`)
        main_key.classList.add("disabledbutton")
        char = ""
       

    }

    el.innerHTML = `<div data-char="${char}">${char}</div>`

    document.getElementById('char_row').appendChild(el)
    el.onclick = function(el) {
        // console.log('Element clicked', char)
        variable.add(char)
        const variables = Array.from(variable).join('');
        console.log('Variables', typeof(variables), variables)
        
        
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

var modalWrap = null;
const warningModal = (title, desc) => {
    if (modalWrap !== null) {
        modalWrap.remove()
    }

    modalWrap = document.createElement('div');
    modalWrap.innerHTML = `
    <div class="modal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">${title}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>${desc}.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" data-bs-dismiss="modal" class="btn btn-primary">Yep</button>
            </div>
            </div>
        </div>
    </div>
    `;
    document.body.append(modalWrap);

    var modal = new bootstrap.Modal(modalWrap.querySelector('.modal'))
    modal.show();
}
