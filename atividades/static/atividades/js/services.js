let areas = document.querySelector('#id_area'),
    subAreas = document.querySelector('#id_sub_area');

// CRUD AREAS

function getAreas() {
    let url = '/api/areas/';

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
    input.value = null;
}

function create(type) {
    let url = `/api/${type}s/`,
        csrf = document.querySelector('[name=csrfmiddlewaretoken]').value,
        nome = document.querySelector(`#api-${type}-nome`),
        descricao = document.querySelector(`#api-${type}-descricao`),
        cor = document.querySelector(`#api-${type}-cor`);

        if (type === 'area') {
            body = jsonArea(nome, descricao, cor);
        }

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

    toggle(`form-${type}`);
    nome.value = null;
    descricao.value = null;

    if (type === 'area') {
        cor.value = '#000000';
        getAreas();
    }
}

function jsonArea(nome, descricao, cor) {
    return JSON.stringify({
        nome: nome.value,
        descricao: descricao.value,
        cor: cor.value
    });
}

function jsonSubArea(nome, descricao, areas) {
    return JSON.stringify({
        nome: nome.value,
        descricao: descricao.value,
        areas: areas.value
    });
}

// CRUD SUB-AREAS

function getSubAreas() {
    const url = '/api/areas/',
        areas = document.querySelector('#api-subarea-areas');

    fetch(url)
        .then(response => response.json())
        .then(dados => {
            renderAreas(areas, dados);
        })
}

function renderAreas(htmlObj, dados){
    for ([index, i] of dados.entries()) {
        const check = document.createElement('input'),
            label = document.createElement('label'),
            br = document.createElement('br');
        check.type = 'checkbox';
        check.name = i.nome;
        check.value = i.id;
        check.id = `check-areas-${index}`;
        label.htmlFor = `check-areas-${index}`;
        label.innerHTML = i.nome;
        htmlObj.appendChild(check);
        htmlObj.appendChild(label);
        htmlObj.appendChild(br);
    }
}

function getSubAreasRelacionadas() {
    let areaId = document.getElementById('id_area').selectedIndex,
        url = `/api/areas/${areaId}/subareas/`;

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

areas.addEventListener('focusout', function(){
    getSubAreasRelacionadas();
});

// Resolver com importação

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
