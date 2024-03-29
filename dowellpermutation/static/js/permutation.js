// Variable declarationvar
var msg = null

let keys = document.querySelectorAll('.key--letter');
const n_data = localStorage.getItem("n");
const r_data = localStorage.getItem("r");
const permutation_data = localStorage.getItem("result");
const charstore = document.getElementById('charstore')
const result_row = document.getElementById('result_row');
const select_n = document.getElementById('select_n');
const select_r = document.getElementById('select_r');
const select_any = document.getElementById('select_any');
select_n.innerHTML = `Select ${n_data} variables from the keyboard above`;

// where to append the selected characters
const selectedChars = new Set();
const selectedChars2 = new Set();
const variable = new Set();
const combination_set = new Set();

let count = 0;
let el_count = 0;


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



//3
const do_permutation = (variables) => {
    console.log("variables", variables)

    //increase count by 1 and save to local storage
    count += 1;
    localStorage.setItem("count", count);
    const count_data = localStorage.getItem("count");

    if (count_data <= r_data) {
        $.ajax({
            url: 'https://100050.pythonanywhere.com/calculator/calculateperm/',
            type: 'POST',
            data: {
                char: variables,
            },
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            success: function (data) {
                console.log(data)
                appendData(data)
            },
            error: function (data) {
                console.log(data)
            },
        })
    }
    else {
        msg = `Not allowed, you can't select more than ${r_data} variables`
        warningModal('Invalid Input', msg)

    }


}

//4
const appendData = (data) => {
    const show_d = document.getElementById('show')
    //clear the previous data
    show_d.innerHTML = ""

    //check if the length of the data is one create a div and append it
    if (data.length == 1) {
        var el = document.createElement("div");
        el.classList.add("key--letter");
        el.innerHTML = `<div data-char="${data}">${data}</div>`
        show_d.appendChild(el)
        el.onclick = function (el) {
            saveData(data)
        }
        //also display small message below this element
        const msg = `<span>Click on the character to save it<span>`;
        const msg_con = document.getElementById('msg')
        msg_con.innerHTML = '';
        msg_con.innerHTML = msg;

    }
    else {
        for (let i = 0; i < data.length; i++) {
            var el = document.createElement("div");
            el.classList.add("key--letter");
            el.innerHTML = `<div data-char="${data[i]}">${data[i]}</div>`
            show_d.appendChild(el)
            el.onclick = function (el) {
                saveData(data[i])
            }
            //also display small message below this element
            const msg = `<span>Click on the any character from above to save it<span>`;
            const msg_con = document.getElementById('msg')
            msg_con.innerHTML = '';
            msg_con.innerHTML = msg;
        }
    }

}

//5
const saveData = (data) => {
    console.log("save data", data)
    $.ajax({
        url: 'https://100050.pythonanywhere.com/calculator/permutations/save/',
        type: 'POST',
        data: {
            char: data,
        },
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function (data) {
            console.log("resp from save :", data);
            appendData2(data);
        },
        error: function (data) {
            console.log(data)
        },
    })
}

//4
const appendData2 = (data) => {
    const show_d = document.getElementById('show')
    //clear the previous data
    show_d.innerHTML = ""

    //check if the length of the data is one create a div and append it
    if (data.length == 1) {
        var el = document.createElement("div");
        el.classList.add("key--letter");
        el.innerHTML = `<div data-char="${data}">${data}</div>`
        show_d.appendChild(el)
        el.onclick = function (el) {
            saveData(data)
        }
        const msg = `<span>Now Select any variable from above<span>`;
        const msg_con = document.getElementById('msg')
        msg_con.innerHTML = '';
        msg_con.innerHTML = msg;

    }
    else {
        var el = document.createElement("div");
        el.classList.add("key--letter");
        // for (let i = 0; i < data.length; i++) {
        //     el.innerHTML = `<div data-char="${data[i]}">${data[i]}</div>`
        // }
        el.innerHTML = `<div data-char="${data}">${data}</div>`
        show_d.appendChild(el)
        el.onclick = function (el) {
            saveData(data[i])
        }
        const msg = `<span>Now Select any variable from above<span>`;
        const msg_con = document.getElementById('msg')
        msg_con.innerHTML = '';
        msg_con.innerHTML = msg;
    }

}

//whenever page refresh send a request to the server to clear session in the server

const clearSession = () => {
    $.ajax({
        url: 'https://100050.pythonanywhere.com/calculator/clear_session/',
        type: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function (data) {
            console.log(data)
        },
        error: function (data) {
            console.log(data)
        }
    })
}

//call the clear session function on page load
clearSession()

// create a helper function
const setAttributes = (el, attrs) => {
    for (var key in attrs) {
        el.setAttribute(key, attrs[key]);
    }
}



const removeEl = (el) => {
    el.remove();
}

const setResult = (combination_set, res) => {
    combination_set.add(data.data)
    return combination_set
}



//2
const createEl = (char) => {

    //increase count by 1 and save to local storage
    el_count += 1;
    localStorage.setItem("el_count", el_count);

    var card_body = document.getElementById('card_body')
    var el = document.createElement("div");
    el.classList.add("key--letter");
    selectedChars.add(char)

    if (selectedChars.size > n_data) {
        msg = `Not allowed, you can't select more than ${n_data} variables`
        warningModal('Invalid Input', msg)
        main_key.classList.add("disabledbutton")
        char = ""
        select_r.innerHTML = `Select any ${r_data} variables from the above selected variables`;
        return
    }

    el.innerHTML = `<div data-char="${char}">${char}</div>`
    document.getElementById('char_row').appendChild(el)
    el.onclick = function (el) {
        if (localStorage.getItem("el_count") <= n_data - 1) {
            warningModal('Invalid Input', `Please select atleast ${n_data} variables first`)
            return
        }
        else {
            do_permutation(char)
            this.classList.add("disabledbutton")
        }

    }
}


//1
for (var x = 0; x < keys.length; x++) {
    keys[x].onclick = function () {
        let char = this.getAttribute('data-char')
        createEl(char)
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



