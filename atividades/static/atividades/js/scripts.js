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
    let subMenu = document.querySelector(`#${id}`),
        subMenuButton = document.querySelector(`#${id}-button`);

    if (subMenu.classList.length === 0) {
        subMenu.classList.add('toggled');
        subMenuButton.lastElementChild.lastElementChild.outerHTML = "<i class='fa-solid fa-angle-down'></i>";
    } else {
        subMenu.classList.remove('toggled');
        subMenuButton.lastElementChild.lastElementChild.outerHTML = "<i class='fa-solid fa-angle-up'></i>";
    }
}

function toggleProfile(id) {
    let element = document.querySelector(`#${id}`);

    if (element.classList.length === 0) {
        element.classList.add('toggled');
    } else {
        element.classList.remove('toggled');
    }
}

function toggleNavegacao(id) {
    let navegacao = document.querySelector(`#${id}`),
        navegacaoButton = document.querySelector(`#${id}-button`),
        i,
        j;

    if (navegacao.classList.length === 1) {
        navegacao.classList.add('toggled');
        navegacaoButton.children[0].outerHTML = '<i class="fa-solid fa-angles-down" onclick="toggleNavegacao(\'navegacao\')"></i>';
        for (i = 0; i < navegacao.children.length; i++) {
            navegacao.children[i].classList.add('toggled');
        }
    } else {
        navegacao.classList.remove('toggled');
        navegacaoButton.children[0].outerHTML = '<i class="fa-solid fa-angles-up" onclick="toggleNavegacao(\'navegacao\')"></i>';
        for (i = 0; i < navegacao.children.length; i++) {
            navegacao.children[i].classList.remove('toggled');
        }
    }
}

let sidebarButton = document.querySelector('#sidebar-button'),
    searchButton = document.querySelector('#search-button'),
    body = document.getElementsByTagName('body')[0];


sidebarButton.addEventListener('click', () => {
    toggleSidebar();
});


(window.onresize = () => {
    let boxes = [
        document.getElementById('tempo-area'),
        document.getElementById('graphic')
    ];
    //console.log(boxes[2].width)
    //console.log(window.innerWidth)
    
    if (body.clientWidth < 1200) {
        recallSidebar();
        for (box of boxes) {
            if (box) {
                box.style.width = 'calc(100% - 20px)';
            }
        }
    } else {
        expandSidebar();
        for (box of boxes) {
            if (box) {
                box.style.width = 'calc(55% - 20px)';
            }
        }
    }
})();


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