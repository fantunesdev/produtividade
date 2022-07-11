import * as services from './services.js';
import * as general from './general.js';
import * as classes from './classes.js'


export function renderDefaultOption(input) {
    let option;

    option = document.createElement('option');
    option.value = 0;
    option.text = '---------';
    input.add(option, input.options[0]);
}


export function options(objectList, input) {
    let option,
        item;

    input.length = 0;
    renderDefaultOption(input);

    for (item of objectList) {
        option = document.createElement('option');
        option.value = item.id;
        option.text = item.nome;
        input.add(option, input.options[item.id]);
    }
    input.selectedIndex = 0;
}


export function select(father, areasList, type) {
    const select = document.createElement('select'),
        label = document.createElement('label');
    
    
    label.innerHTML = 'Áreas:';
    select.classList.add('form-control');
    select.id = `id-${type}-nome`;
    label.htmlFor = `id-${type}-nome`;
    label.appendChild(select);

    father.appendChild(label);
    defaultOption(select);
    options(areasList, select);
}


export function checkbox(father, areasList, type) {
    let div, item, check, label, br, idCheck;

    div = document.createElement('div');
    label = document.createElement('label');
    br = document.createElement('br');

    div.id = `${type}-areas-checkbox-list`;

    father.appendChild(div);

    label.innerHTML = 'Áreas:'
    div.appendChild(label);
    div.appendChild(br);

    for (item of areasList) {
        label = document.createElement('label'),
        check = document.createElement('input'),
        br = document.createElement('br'),
        idCheck = `id-${type}-area-${general.slugify(item.nome)}`;
        label.innerHTML = item.nome;
        label.htmlFor = idCheck;
        check.type = 'checkbox';
        check.id = idCheck;
        check.value = item.id;
        div.appendChild(check);
        div.appendChild(label)
        div.appendChild(br);
    }
}


export function box(father, type) {
    const boxForm = document.querySelector(`#form-${type}`);

    if (boxForm) {
        father.removeChild(boxForm);
    } else {
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
                    boxSection.id = `id-box-${type}-title`;
                    break;
                case 1:
                    boxSection.classList.add('box-body');
                    boxSection.id = `id-box-${type}-body`;
                    break;
                case 2:
                    boxSection.classList.add('box-footer');
                    boxSection.id = `id-box-${type}-footer`;
                    break;
            }
            box.appendChild(boxSection);
        }
    }
    return document.querySelector(`#form-${type}`)
}


export function boxTitle(father, value) {
    const title = document.createElement('h3');
    title.innerHTML = value;
    father.appendChild(title);
}


export function inputs(father, type) {
    for (let i = 0; i < 3; i++) {
        const input = document.createElement('input'),
            label = document.createElement('label'),
            textArea = document.createElement('textarea');
        switch (i) {
            case 0:
                input.type = 'hidden';
                input.id = `id-${type}-id`;
                input.value = null;
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
                label.innerHTML = 'Descrição:'
                textArea.classList.add('form-control');
                textArea.classList.add('textarea')
                textArea.id = `id-${type}-descricao`;
                label.htmlFor = `id-${type}-descricao`;
                label.appendChild(textArea);
                break;               
        }
        father.appendChild(label);
    }
}


export function areaOptions(father, areasList, type) {
    const input = document.createElement('input'),
        label = document.createElement('label');
    
    label.innerHTML = 'Área:';
    input.type = 'select';
    input.id = `id-${type}-area`;
    input.classList.add('form-control');
    label.htmlFor = `id-${type}-area`;
    label.appendChild(input);

    options(areasList, `#${father.id}`)
    father.appendChild(label);
}


export function colorInput(father, type) {
    const input = document.createElement('input'),
        label = document.createElement('label');
    
    label.innerHTML = 'Cor:';
    input.type = 'color';
    input.id = `id-${type}-cor`;
    input.classList.add('form-control');
    label.htmlFor = `id-${type}-cor`;
    label.appendChild(input);
    father.appendChild(label);
}


export function submit(father, type, action) {
    const button = document.createElement('input'),
        input = document.querySelector(`#id_${type}`);
    

    button.type = 'button';
    button.classList.add('btn', 'btn-primary');
    button.id = `post-${type}-button`
    switch (action) {
        case 'create':
            button.value = 'Cadastrar';
            button.addEventListener('click', event => {
                create(type);
            });
            break;
        case 'update':
            button.value = 'Atualizar';
            button.addEventListener('click', event => {
                update(type);
            })
            break;
    }
    father.appendChild(button);  
}


async function create(type) {
    const object = readInputs(type),
        csrf = document.querySelector('[name=csrfmiddlewaretoken]').value,
        father = document.querySelector(`#div-${type}`),
        box = document.querySelector(`#form-${type}`);

    // fazer validação dos inputs dos formulários

    if (type === 'area') {
        const area = await services.createArea(object, csrf),
            areas = await services.getAreas();

        father.removeChild(box);
        alert(`A área ${area.nome} foi criada com sucesso.`);
        options(areas, classes.area.select);
    } else if (type === 'subarea') {
        const subarea = await services.createSubarea(object, csrf),
            subareas = await services.getSubareasArea(classes.area.select.selectedIndex);

        father.removeChild(box);
        alert(`A sub-área ${subarea.nome} foi criada com sucesso.`);
        options(subareas, classes.subarea.select);
    } else if (type === 'plataforma') {
        const plataforma = await services.createPlataforma(object, csrf),
            plataformas = await services.getPlataformasArea(classes.area.select.selectedIndex);

        father.removeChild(box);
        alert(`A plataforma ${plataforma.nome} foi criada com sucesso.`);
        options(plataformas, classes.plataforma.select);
    } else if (type === 'pessoa') {
        const pessoa = await services.createPessoa(object, csrf),
            pessoas = await services.getPessoasArea(classes.area.select.selectedIndex);

        father.removeChild(box);
        alert(`A pessoa ${pessoa.nome} foi criada com sucesso.`);
        options(pessoas, classes.pessoa.select);
    }
}


async function update(type) {
    const object = readInputs(type),
        csrf = document.querySelector('[name=csrfmiddlewaretoken]').value,
        father = document.querySelector(`#div-${type}`),
        box = document.querySelector(`#form-${type}`);

    // fazer validação dos inputs dos formulários

    if (type === 'area') {
        const area = await services.updateArea(object, csrf),
            areas = await services.getAreas();

        father.removeChild(box);
        alert(`A área ${area.nome} foi atualizada com sucesso.`);
        options(areas, classes.area.select);

    } else if (type === 'subarea') {
        const subarea = await services.updateSubarea(object, csrf),
            idArea = classes.area.select.value;

        alert(`A sub-área ${subarea.nome} foi atualizada com sucesso.`);
        if (idArea) {
            var subareas = await services.getSubareasArea(classes.area.select.value);
        }
        father.removeChild(box);
        options(subareas, classes.subarea.select);

    } else if (type === 'plataforma') {
        const plataforma = await services.updatePlataforma(object, csrf),
            idArea = classes.area.select.value;
            
        alert(`A plataforma ${plataforma.nome} foi atualizada com sucesso.`);
        if (idArea) {
            var plataformas = await services.getPlataformasArea(classes.area.select.value);
        }
        father.removeChild(box);
        options(plataformas, classes.plataforma.select);

    } else if (type === 'pessoa') {
        const pessoa = await services.updatePessoa(object, csrf),
            idArea = classes.area.select.value;

        alert(`A pessoa ${pessoa.nome} foi atualizada com sucesso.`);
        if (idArea) {
            var pessoas = await services.getPessoasArea(classes.area.select.value);
        }
        father.removeChild(box);
        options(pessoas, classes.pessoa.select);

    }
}


export async function instanceInputs(type, input) {
    const idInput = document.querySelector(`#id-${type}-id`),
        nomeInput = document.querySelector(`#id-${type}-nome`),
        descricaoInput = document.querySelector(`#id-${type}-descricao`),
        corInput = document.querySelector(`#id-${type}-cor`),
        areasDiv = document.querySelector(`#${type}-areas-checkbox-list`),
        father = document.querySelector(`#div-${type}`),
        box = document.querySelector(`#form-${type}`);

    if (input.value) {
        if (type === 'area') {
            var object = await services.getAreaId(input.value);
        } else if (type === 'subarea') {
            var object = await services.getSubareaId(input.value);
        } else if (type === 'plataforma') {
            var object = await services.getPlataformaId(input.value);
        } else if (type === 'pessoa') {
            var object = await services.getPessoaId(input.value);
        }
    
        idInput.value = object.id;
        nomeInput.value = object.nome;
        descricaoInput.value = object.descricao;

        if (corInput) {
            corInput.value = object.cor;
        }

        if (areasDiv) {
            for (let item of areasDiv.children) {
                if (item.type === 'checkbox') {
                    for (let i = 0; i < object.areas.length; i++) {
                        if (object.areas[i] === parseInt(item.value)) {
                            item.checked = true;
                        }
                    }
                }                
            }
        }
    } else {
        alert(`Selecione uma ${type}.`)
        father.removeChild(box);
    }
}


function readInputs(type) {
    const idInput = document.querySelector(`#id-${type}-id`),
        nomeInput = document.querySelector(`#id-${type}-nome`),
        descricaoInput = document.querySelector(`#id-${type}-descricao`),
        corInput = document.querySelector(`#id-${type}-cor`),
        areasDiv = document.querySelector(`#${type}-areas-checkbox-list`);
    let areasList = [];

    if (areasDiv) {
        for (let item of areasDiv.children) {
            if (item.checked) {
                areasList.push(parseInt(item.value))
            }
        }
    }

    if (type === 'area') {
        var object = {
            nome: nomeInput.value,
            descricao: descricaoInput.value,
            cor: corInput.value
        };
    } else {
        var object = {
            nome: nomeInput.value,
            descricao: descricaoInput.value,
            areas: areasList
        };
    }
    if (idInput.value) {
        object.id = idInput.value;
    }
    
    return JSON.stringify(object);
}