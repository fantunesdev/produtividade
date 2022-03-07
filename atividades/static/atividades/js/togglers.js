export function mostrar(id){
    if(document.getElementById(id).style.display === 'block'){
        document.getElementById(id).style.display = 'none';
    }else{
        document.getElementById(id).style.display = 'block';
    }
}

export function sidebar(){
    let navegacao = document.getElementById('navegacao'),
        logo = document.getElementById('logo'),
        userPanel = document.getElementById('user-panel'),
        asideProfilePhoto = document.getElementById('aside-profile-photo'),
        asideProfileName = document.getElementById('aside-profile-name'),
        conteudo = document.getElementById('conteudo');

    if(navegacao.style.width === '52px'){
        navegacao.style.width = '230px';
        logo.style.marginLeft = '0px';
        userPanel.style.height = '70px';
        asideProfilePhoto.style.height = '50px';
        asideProfilePhoto.style.width = '50px';
        asideProfileName.style.display = 'inline-block';
        conteudo.style.width = 'calc(100% - 230px)';
    }else{
        navegacao.style.width = '52px';
        logo.style.marginLeft = '-230px';
        userPanel.style.height = '60px';
        asideProfilePhoto.style.height = '35px';
        asideProfilePhoto.style.width = '35px';
        asideProfileName.style.display = 'none';
        conteudo.style.width = 'calc(100% - 52px)';
    }
}

export function profile(){
    let profile = document.getElementById('profile'),
        nome = document.getElementById('nome'),
        mail = document.getElementById('mail'),
        photo = document.getElementById('photo'),
        desde = document.getElementById('desde'),
        footerLeft = document.getElementById('footer-left'),
        footerRight = document.getElementById('footer-right');


    if(profile.style.height === '290px'){
        nome.style.display = 'none';
        mail.style.display = 'none';
        photo.style.display = 'none';
        desde.style.display = 'none';
        footerLeft.style.display = 'none';
        footerRight.style.display = 'none';
        profile.style.height = '0px';
        profile.style.width = '0px'
    }else{
        nome.style.display = 'block';
        mail.style.display = 'block';
        photo.style.display = 'block';
        desde.style.display = 'block';
        footerLeft.style.display = 'block';
        footerRight.style.display = 'block';
        profile.style.height = '290px';
        profile.style.width = '340px'
    }
}

let sidebarButton = document.querySelector('#sidebar-button'),
    profileButton = document.querySelector('#profile-button');

sidebarButton.addEventListener('click', function(){
    sidebar();
});

profileButton.addEventListener('click', function(){
    profile();
});
