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
        nome = document.querySelector(`#id-${type}-nome`),
        descricao = document.querySelector(`#id-${type}-descricao`),
        cor = document.querySelector(`#id-${type}-cor`);

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
}

function renderAreas(htmlObj){
    const url = '/api/areas/',
        father = htmlObj.appendChild(document.createElement('label')),
        br = document.createElement('br');

    father.innerHTML = "Áreas:";
    father.appendChild(br);
    
    fetch(url)
        .then(response => response.json())
        .then(dados => {
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
                father.appendChild(check);
                father.appendChild(label);
                father.appendChild(br);
            }
        });
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

function renderForm(type, action) {
    const father =  document.querySelector(`#div-${type}`);

    if (father.children[5]) {
        father.children[5].parentNode.removeChild(father.children[5]);
    } else {
        renderBox(type, father);
        renderBoxTitle(type, father.children[5].children[0]);
        renderInputs(type, father.children[5].children[1]);
    
        if (type === 'subarea') {
            const divAreasSubArea = document.createElement('div');
            divAreasSubArea.id = 'div-area-subarea';
    
            father.children[5].children[1].appendChild(divAreasSubArea);
            renderAreas(divAreasSubArea);
    
            renderButton(type, father.children[5].children[2], action);
        
        }
    }
}

function renderBox(type, father) {
    const box = document.createElement('div');
    
    box.classList.add('box');
    box.classList.add('box-primary', 'box-max-width-920px', 'center-div')
    box.id = `form-${type}`;

    father.appendChild(box);
    
    for (let i = 0; i < 3; i++) {
        let boxSection = document.createElement('div');
        
        switch (i) {
            case 0:
                boxSection.classList.add('box-title');
                boxSection.id = 'id-box-title';
                break;
            case 1:
                boxSection.classList.add('box-body');
                boxSection.id = 'id-box-body';
                break;
            case 2:
                boxSection.classList.add('box-footer');
                boxSection.id = 'id-box-footer';
                break;
        }
        box.appendChild(boxSection);
    }
}

function renderBoxTitle(type, father) {
    h3 = document.createElement('h3');
    switch (type) {
        case 'area':
            h3.innerHTML = 'Cadastrar Área';
            break;
        case 'subarea':
            h3.innerHTML = 'Cadastrar Sub-Área';
    }
    father.appendChild(h3);
}

function renderInputs(type, father) {
    for (let i = 0; i < 3; i++) {
        let input = document.createElement('input'),
            label = document.createElement('label');
        switch (i) {
            case 0:
                input.type = 'hidden';
                input.id = `id-${type}-id`;
                label.appendChild(input);
                break;
            case 1:
                label.innerHTML = 'Nome:';
                input.classList.add('form-control');
                input.id = `id-${type}-nome`;
                label.htmlFor = `id-${type}-nome`;
                label.appendChild(input);
                break;
            case 2:
                label.innerHTML = 'Descricao:'
                input.classList.add('form-control');
                input.id = `id-${type}-descricao`;
                label.htmlFor = `id-${type}-descricao`;
                label.appendChild(input);
                break;               
        }
        father.appendChild(label);
    }
}

function renderButton(type, father, action) {
    const button = document.createElement('input');

    button.type = 'button';
    button.classList.add('btn', 'btn-primary');
    button.id = 'form-button'
    switch (action) {
        case 'create':
            button.value = 'Cadastrar';
            button.onclick = () => {
                alert('Função não desenvolvida');
            }
            break;
        case 'update':
            button.value = 'Atualizar';
            button.onclick = () => {
                alert('Função não desenvolvida');
            }
            break;
    }
    father.appendChild(button);

}
