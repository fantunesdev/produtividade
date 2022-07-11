import * as services from './services.js';
import * as render from './render.js';


export const area = {
    button: {
        create: document.querySelector('#create-area'),
        update: document.querySelector('#update-area'),
        list: document.querySelector('#list-area'),
    },
    select: document.querySelector('#id_area'),
    div: document.querySelector('#div-area'),

    async renderSelect() {
        const areasList = await services.getAreas();
        
        render.options(areasList, this.select);
    },

    renderForm(action) {
        const type = 'area',
            box = render.box(this.div, type);

        if (box) {
            const boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2]
            render.boxTitle(boxTitle, 'Cadastrar Área');
            render.inputs(boxBody, type);
            render.colorInput(boxBody, type);
            render.submit(boxFooter, type, action);
            if (action === 'update') {
                render.instanceInputs(type, this.select);
            }
        }
    }
    
}

area.button.create.addEventListener('click', () => area.renderForm('create'));
area.button.update.addEventListener('click', () => area.renderForm('update'))
area.button.list.addEventListener('click', () => area.renderSelect());
area.select.addEventListener('focusout', () => {
    if (area.select.value !== '') {
        subarea.renderSelect();
        plataforma.renderSelect();
        pessoa.renderSelect();
    } else {
        render.options([], subarea.select);
        render.options([], plataforma.select);
        render.options([], pessoa.select);
    }
});


export const subarea = {
    button: {
        create: document.querySelector('#create-subarea'),
        update: document.querySelector('#update-subarea'),
        list: document.querySelector('#list-subarea'),
    },
    select: document.querySelector('#id_subarea'),
    div: document.querySelector('#div-subarea'),
    
    async renderSelect() {
        if (area.select.value !== '') {
            let areaId = area.select.value;
            const subareas = await services.getSubareasArea(areaId);
        
            render.options(subareas, this.select);
        } else {
            render.options([], this.select)
            alert('Selecione uma área válida e tente novamente.')
        }
    },

    async renderForm(action) {
        const areasList = await services.getAreas(),
            type = 'subarea',
            box = render.box(this.div, type);

        if (box) {
            const boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2]
            render.boxTitle(boxTitle, 'Cadastrar Sub-Área');
            render.inputs(boxBody, type);
            render.checkbox(boxBody, areasList, type);
            render.submit(boxFooter, type, action)
            if (action === 'update') {
                render.instanceInputs(type, this.select);
            }
        }
    },
}

subarea.button.create.addEventListener('click', () => subarea.renderForm('create'));
subarea.button.update.addEventListener('click', () => subarea.renderForm('update'));
subarea.button.list.addEventListener('click', () => subarea.renderSelect());


export const plataforma = {
    button: {
        create: document.querySelector('#create-plataforma'),
        update: document.querySelector('#update-plataforma'),
        list: document.querySelector('#list-plataforma'),
    },
    select: document.querySelector('#id_plataforma'),
    div: document.querySelector('#div-plataforma'),

    async renderSelect() {
        if (area.select.value) {
            let areaId = area.select.value;
            const plataformas = await services.getPlataformasArea(areaId);
            
            render.options(plataformas, this.select);
        } else {
            render.options([], this.select)
            alert('Selecione uma área válida e tente novamente.')
        }
    },

    async renderForm(action) {
        const areasList = await services.getAreas(),
            type = 'plataforma',
            box = render.box(this.div, type);

        if (box) {
            const boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2]
            render.boxTitle(boxTitle, 'Cadastrar Plataforma');
            render.inputs(boxBody, type);
            render.checkbox(boxBody, areasList, type);
            render.submit(boxFooter, type, action)
            if (action === 'update') {
                render.instanceInputs(type, this.select);
            }
        }
    }
}

plataforma.button.create.addEventListener('click', () => plataforma.renderForm('create'));
plataforma.button.update.addEventListener('click', () => plataforma.renderForm('update'));
plataforma.button.list.addEventListener('click', () => plataforma.renderSelect());

export const pessoa = {
    button: {
        create: document.querySelector('#create-pessoa'),
        update: document.querySelector('#update-pessoa'),
        list: document.querySelector('#list-pessoa'),
    },
    select: document.querySelector('#id_pessoa'),
    update: document.querySelector('#list-pessoa'),
    div: document.querySelector('#div-pessoa'),

    async renderSelect() {
        if (area.select.value) {
            let areaId = area.select.value;
            const pessoas = await services.getPessoasArea(areaId);
        
            render.options(pessoas, this.select);
        } else {
            render.options([], this.select)
            alert('Selecione uma área válida e tente novamente.')
        }
    },

    async renderForm(action) {
        const areasList = await services.getAreas(),
            type = 'pessoa',
            box = render.box(this.div, type);

        if (box) {
            const boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2]
            render.boxTitle(boxTitle, 'Cadastrar Pessoa');
            render.inputs(boxBody, type);
            render.checkbox(boxBody, areasList, type);
            render.submit(boxFooter, type, action)
            if (action === 'update') {
                render.instanceInputs(type, this.select);
            }
        }
    }
}

pessoa.button.create.addEventListener('click', () => pessoa.renderForm('create'));
pessoa.button.update.addEventListener('click', () => pessoa.renderForm('update'));
pessoa.button.list.addEventListener('click', () => pessoa.renderSelect());
