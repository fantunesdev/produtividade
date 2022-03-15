let areas = document.querySelector('#id_area'),
    subAreas = document.querySelector('#id_sub_area');

function getAreas() {
    let url = '/api/areas/',
        areasOption,
        i;

    fetch(url)
        .then(response => response.json())
        .then(dados => {
            areas.length = 0;
            createOptions(dados, 'id_area');
        });
}

function createOptions(list, htmlId) {
    let input = document.getElementById(htmlId),
        option,
        i;

    for (i = 0; i < list.length; i++) {
        option = document.createElement('option');
        option.value = list[i].id;
        option.text = list[i].nome;
        input.add(option, input.options[i]);
    }
}

function createArea() {
    let url = '/api/areas/',
        csrf = document.querySelector('[name=csrfmiddlewaretoken]').value,
        nome = document.querySelector('#api-area-nome'),
        descricao = document.querySelector('#api-area-descricao'),
        cor = document.querySelector('#api-area-cor');

        body = JSON.stringify({
            nome: nome.value,
            descricao: descricao.value,
            cor: cor.value
        });

        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        };

        requestOptions = {
            method: 'POST',
            headers: headers,
            body: body,
        };

    fetch(url, requestOptions)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });

    toggle('form-area');
    getAreas();
    nome.value = null;
    descricao.value = null;
    cor.value = '#000000';
}



function getSubAreasRelacionadas() {
    let areaId = document.getElementById('id_area').selectedIndex,
        url = `/api/areas/${areaId}/subareas/`,
        subAreaOption,
        i;

    fetch(url)
        .then(response => response.json())
        .then(dados => {
            subAreas.length = 0;
            createOptions(dados, 'id_sub_area')
            subAreas.value = null;
        });
}

function update(boxId, type) {
    let typeId = document.getElementById(boxId).selectedIndex;

    if (type === 'subarea') {
        typeId += 1;
    }

    let url = `/api/${type}s/${typeId}`;

    if (typeId) {
        toggle(`form-${type}`);
        fetch(url)
            .then(response => response.json())
            .then(dados => {
                console.log
                document.getElementById(`api-${type}-id`).value = dados.id;
                document.getElementById(`api-${type}-nome`).value = dados.nome;
                document.getElementById(`api-${type}-descricao`).value = dados.descricao;
                if (type === 'area') {
                    document.getElementById('api-area-cor').value = dados.cor;
                } else if (type === 'subarea') {
                    for (i of dados.areas) {
                        document.createElement('input')
                    }
                    document.getElementById('api-subarea-area').value = dados.areas;
                }
            });
    } else {
        alert(`Você não selecionou nenhuma ${type} para editar.`);
    }
}

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

areas.addEventListener('focusout', function(){
    getSubAreasRelacionadas();
});