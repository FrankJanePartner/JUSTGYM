function openSignupPopup() {
    document.getElementById('signupPopup').style.display = 'block';
}
function openSignupSucssessPopup() {
    document.getElementById('signupSucessPopup').style.display = 'block';
}

function openLoginPopup() {
    document.getElementById('loginPopup').style.display = 'block';
}

function openSort() {
    document.getElementById('Sort').style.display = 'block';
}
function dropdown() {
    var dropList = document.getElementById('dropList');
    if (dropList.style.display === 'none' || dropList.style.display === '') {
        dropList.style.display = 'block';
    } else {
        dropList.style.display = 'none';
    }
}

function dropdown1() {
    var dropList1 = document.getElementById('dropList1');
    if (dropList1.style.display === 'none' || dropList1.style.display === '') {
        dropList1.style.display = 'block';
    } else {
        dropList1.style.display = 'none';
    }
}


function closePopup(popupId) {
    document.getElementById(popupId).style.display = 'none';
}
