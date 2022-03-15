let url;


switch (window.location.pathname) {
    case '/atividades/':
        url = "/api/atividades/"
        break;

    default:
        break;
}

console.log(url)
fetch(url)
.then(response => response.json())
.then(content => console.log(content))