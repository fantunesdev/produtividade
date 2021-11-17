var ctx = document.getElementsByClassName("line-chart")

            // Type, Data e Options
            var chartGraph = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ["Conhecimento", "Empreendedorismo", "Saúde", "Finanças", "Tecnologia", "Música"],
                    datasets: [
                        {
                        label: "ÁREAS",
                        data: [
                                {{ areas.conhecimento }},
                                {{ areas.empreendedorismo }},
                                {{ areas.saude}},
                                {{ areas.financas }},
                                {{ areas.tecnologia}},
                                {{ areas.musica }}
                               ],
                        borderWidth: 6,
                        borderColor: [
                                      'rgba(75,0,130,0.85)',
                                      'rgba(0,0,128,0.85)',
                                      'rgba(0,100,0,0.85)',
                                      'rgba(255,215,0,0.85)',
                                      'rgba(255,140,0,0.85)',
                                      'rgba(178,34,34,0.85)',
                                     ],
                        backgroundColor: [
                                      'rgba(75,0,130,0.85)',
                                      'rgba(0,0,128,0.85)',
                                      'rgba(0,100,0,0.85)',
                                      'rgba(255,215,0,0.85)',
                                      'rgba(255,140,0,0.85)',
                                      'rgba(178,34,34,0.85)',
                                     ],
<!--                        minBarLength: 80,-->
                        }
                        ]
                },
                options: {
                    title: {
                        display: true,
                        fontSize: 20,
                        text: "PRODUTIVIDADE POR ÁREA"
                    }
                },
                labels: {
                    fontStyle: "bold"
                }
            });
