var ctx = document.getElementsByClassName("line-chart")
var lista_json = JSON.parse(document.querySelector('#json').value);

let nomes = [],
    valores = [],
    cores = [];

for (i of lista_json) {
    if (i.nome !== 'Total') {
        nomes.push(i.nome);
        valores.push(i.tempo);
        cores.push(i.cor);
    }
}
        // Type, Data e Options
        var chartGraph = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: nomes,
                datasets: [
                    {
                    label: "ÁREAS",
                    data: valores,
                    borderWidth: 6,
                    borderColor: cores,
                    backgroundColor: cores,
                    <!-- minBarLength: 80,-->
                    }
                    ]
            },
            options: {
                title: {
                    display: true,
                    fontSize: 20,
//                    text: "PRODUTIVIDADE POR ÁREA"
                }
            },
            labels: {
                fontStyle: "bold"
            }
        });