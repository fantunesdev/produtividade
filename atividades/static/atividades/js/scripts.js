// import * as Togglers from './togglers.js'

function toggleSidebar() {
    toggle = document.getElementsByClassName('toggle');

    if (body.classList.length === 0) {
        recallSidebar();
    } else {
        expandSidebar();
    }
}

function recallSidebar() {
    let body = document.getElementsByTagName('body')[0],
        logo = document.getElementsByTagName('body')[0].children[1].children[0],
        toggle = document.getElementsByClassName('toggle'),
        inverseToggle = document.getElementsByClassName('inverse-toggle'),
        i;

        body.classList.add('toggled-sidebar');
        logo.children[1].classList.add('toggled');

        for (i of toggle) {
            i.classList.add('toggled');
        }

        for (j of inverseToggle) {
            j.classList.add('toggled')
        }
}

function expandSidebar() {
    let body = document.getElementsByTagName('body')[0],
        logo = document.getElementsByTagName('body')[0].children[1].children[0],
        toggle = document.getElementsByClassName('toggle'),
        inverseToggle = document.getElementsByClassName('inverse-toggle'),
        i;

        body.classList.remove('toggled-sidebar');
        logo.children[1].classList.remove('toggled');

        for (i of toggle) {
            i.classList.remove('toggled');
        }

        for (j of inverseToggle) {
            j.classList.remove('toggled')
        }
}

function toggleSubMenu(id) {
    const subMenu = document.querySelector(`#${id}`),
        subMenuButton = document.querySelector(`#${id}-button`);

    if (hasToggled(subMenu.classList)) {
        subMenu.classList.remove('toggled');
        subMenuButton.lastElementChild.lastElementChild.outerHTML = "<i class='fa-solid fa-angle-up'></i>";
    } else {
        subMenu.classList.add('toggled');
        subMenuButton.lastElementChild.lastElementChild.outerHTML = "<i class='fa-solid fa-angle-down'></i>";
    }
}

function toggleProfile(id) {
    let element = document.querySelector(`#${id}`);

    if (hasToggled(element.classList)) {
        element.classList.remove('toggled');
    } else {
        element.classList.add('toggled');
    }
}

function toggleNavegacao(id) {
    let navegacao = document.querySelector(`#${id}`),
        navegacaoButton = document.querySelector(`#${id}-button`),
        i,
        j;

        
    if (hasToggled(navegacao.classList)) {
        navegacao.classList.remove('toggled');
        navegacaoButton.children[0].outerHTML = '<i class="fa-solid fa-angles-up" onclick="toggleNavegacao(\'navegacao\')"></i>';
        for (i = 0; i < navegacao.children.length; i++) {
            navegacao.children[i].classList.remove('toggled');
        }
        localStorage.setItem('time-navigation-bar-status', 'show');
    } else {
        navegacao.classList.add('toggled');
        navegacaoButton.children[0].outerHTML = '<i class="fa-solid fa-angles-down" onclick="toggleNavegacao(\'navegacao\')"></i>';
        for (i = 0; i < navegacao.children.length; i++) {
            navegacao.children[i].classList.add('toggled');
        }
        localStorage.setItem('time-navigation-bar-status', 'hide');
    }
}

(function showTimeNavigationBar() {
    let id = 'navegacao';
        navigation = document.querySelector(`#${id}`),
        navigationButton = document.querySelector(`#${id}-button`),
        menu = localStorage.getItem('time-navigation-bar-status');
    
    if (navigation) {
        if (menu === 'show') {
            navigation.classList.remove('toggled');
            navigationButton.children[0].outerHTML = '<i class="fa-solid fa-angles-up" onclick="toggleNavegacao(\'navegacao\')"></i>';
            for (let i = 0; i < navigation.children.length; i++) {
                navigation.children[i].classList.remove('toggled');
            }

        }
    }
})();

let sidebarButton = document.querySelector('#sidebar-button'),
    searchButton = document.querySelector('#search-button'),
    body = document.getElementsByTagName('body')[0];


sidebarButton.addEventListener('click', () => {
    toggleSidebar();
});

body.addEventListener('click', event => {
    const toggledables = body.getElementsByClassName('toggler'),
        profile = document.getElementById('profile');
    
    if (event.target.id !== 'profile-photo-button') {
        profile.classList.add('toggled');
    }
});


(window.onresize = () => {
    let boxes = [
        document.getElementById('tempo-area'),
        document.getElementById('graphic')
    ];
    
    if (body.clientWidth < 1200) {
        recallSidebar();
        for (box of boxes) {
            if (box) {
                box.style.maxWidth = 'calc(100% - 20px)';
            }
        }
    } else {
        expandSidebar();
        for (box of boxes) {
            if (box) {
                box.style.maxWidth = 'calc(55% - 20px)';
            }
        }
    }
})();

function toggle(id) {
    let box = document.getElementById(id);

        if (hasToggled(box.classList)) {
            box.classList.remove('toggled');
        } else {
            box.classList.add('toggled');
        }
}

function hasToggled(classList) {
    let list = Array.from(classList);

    return list.includes('toggled');
}

document.addEventListener("DOMContentLoaded", function () {
    var checkboxes = document.querySelectorAll('input[name="dias_da_semana"]');
    
    checkboxes.forEach(function (checkbox) {
      checkbox.addEventListener("change", function () {
        if (this.checked) {
          this.parentNode.classList.add("dias-da-semana-checkbox-checked");
        } else {
          this.parentNode.classList.remove("dias-da-semana-checkbox-checked");
        }
      });
    });
  });


const divDiasDaSemana = document.getElementsByClassName('dias-da-semana')[0].children;
const selecionarTodosBtn = document.getElementById('selecionar-todos-btn');
const diasDaSemanaCheckboxes = document.querySelectorAll('[id^="id_dias_da_semana_"]');
let diasDaSemanaChecked = false;

selecionarTodosBtn.addEventListener('click', () => {
    for (let checkbox of diasDaSemanaCheckboxes) {
        if (diasDaSemanaChecked) {
            checkbox.checked = false;
            checkbox.parentNode.classList.remove('dias-da-semana-checkbox-checked')  ;          
            selecionarTodosBtn.innerHTML = 'Selecionar todos';
        } else {
            checkbox.checked = true;
            checkbox.parentNode.classList.add('dias-da-semana-checkbox-checked');
            selecionarTodosBtn.innerHTML = 'Desmarcar todos';
        }
    }
    diasDaSemanaChecked = !diasDaSemanaChecked;
});


// OBSSOLETO

// searchButton.addEventListener('click', () => {
//     toggleSearch();
// });

// function toggleSearch() {
//     let form = document.getElementById('search-form');
// 
//     if (form.classList[2] === 'toggled') {
//         form.classList.remove('toggled');
//     } else {
//         form.classList.add('toggled');
//     }
// }