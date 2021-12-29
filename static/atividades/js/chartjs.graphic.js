let url = "http://localhost:800/api/atividades"
console.log(url)
fetch(url)
.then(response => response.json())
.then(content => console.log(content))