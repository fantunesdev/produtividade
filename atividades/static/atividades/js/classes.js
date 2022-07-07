import * as services from './services.js';
import * as render from './render.js';


export const area = {
    button: {
        create: document.querySelector('#create-area'),
        list: document.querySelector('#list-area'),
    },
    select: document.querySelector('#id_area'),
    div: document.querySelector('#div-area'),

    async renderSelect() {
        const areasList = await services.getAreas();
        
        render.options(areasList, this.select);
    },

    async renderForm(action) {
        const type = 'area',
            box = render.box(this.div, type);

        if (box) {
            const boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2]
            render.boxTitle(boxTitle, 'Cadastrar Área');
            render.inputs(boxBody, type);
            render.colorInput(boxBody, type);
            render.submit(boxFooter, type, action)
        }
    }
}

area.button.create.addEventListener('click', () => area.renderForm('create'));
area.button.list.addEventListener('click', () => area.renderSelect());
area.select.addEventListener('focusout', () => {
    subarea.renderSelect();
    plataforma.renderSelect();
    pessoa.renderSelect();
});


export const subarea = {
    button: {
        create: document.querySelector('#create-subarea'),
        list: document.querySelector('#list-subarea'),
    },
    select: document.querySelector('#id_subarea'),
    div: document.querySelector('#div-subarea'),
    
    async renderSelect() {
        if (area.select.value) {
            let areaId = area.select.value;
            const subareas = await services.getSubareasArea(areaId);
        
            render.options(subareas, this.select);
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
        }
    }
}

subarea.button.create.addEventListener('click', () => subarea.renderForm('create'));
subarea.button.list.addEventListener('click', () => subarea.renderSelect());


export const plataforma = {
    button: {
        create: document.querySelector('#create-plataforma'),
        list: document.querySelector('#list-plataforma'),
    },
    select: document.querySelector('#id_plataforma'),
    div: document.querySelector('#div-plataforma'),

    async renderSelect() {
        if (area.select.value) {
            let areaId = area.select.value;
            const plataformas = await services.getPlataformasArea(areaId);
            
            render.options(plataformas, this.select);
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
        }
    }
}

plataforma.button.create.addEventListener('click', () => plataforma.renderForm('create'));
plataforma.button.list.addEventListener('click', () => plataforma.renderSelect());

export const pessoa = {
    button: {
        create: document.querySelector('#create-pessoa'),
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
        }
    }
}

pessoa.button.create.addEventListener('click', () => pessoa.renderForm('create'));
pessoa.button.list.addEventListener('click', () => pessoa.renderSelect());
