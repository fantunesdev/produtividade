import * as services from './services.js';
import * as htmlElements from './html-elements.js';

const area = {
    select: document.querySelector('#id_area'),
    update: document.querySelector('#update-area'),

    async renderSelect() {
        const areas = await services.getAreas();
        
        this.select.length = 0;
        htmlElements.renderOptions(areas, this.select.id);
    },
}

const subarea = {
    select: document.querySelector('#id_subarea'),
    update: document.querySelector('#update-subarea'),
    
    async renderSelect() {
        this.select.length = 0;
        htmlElements.renderDefaultOption(this.select.id);
        if (area.select.value) {
            let areaId = area.select.value;
            const subareas = await services.getSubareasArea(areaId);
        
            htmlElements.renderOptions(subareas, this.select.id);
        }
    }
}

const plataforma = {
    select: document.querySelector('#id_plataforma'),
    update: document.querySelector('#update-plataforma'),

    async rendersSelect() {
        this.select.length = 0;
        htmlElements.renderDefaultOption(this.select.id);
        if (area.select.value) {
            let areaId = area.select.value;
            const plataformas = await services.getPlataformasArea(areaId);
            
            htmlElements.renderOptions(plataformas, this.select.id);
        }
    },
}

const pessoa = {
    select: document.querySelector('#id_pessoa'),
    update: document.querySelector('#update-pessoa'),

    async renderSelect() {
        this.select.length = 0;
        htmlElements.renderDefaultOption(this.select.id);
        if (area.select.value) {
            let areaId = area.select.value;
            const pessoas = await services.getPessoasArea(areaId);
        
            htmlElements.renderOptions(pessoas, this.select.id);
        }
    }
}


area.update.addEventListener('click', () => area.renderSelect());
area.select.addEventListener('focusout', () => {
    subarea.renderSelect();
    plataforma.rendersSelect();
    pessoa.renderSelect();
});

subarea.update.addEventListener('click', () => subarea.renderSelect());

plataforma.update.addEventListener('click', () => plataforma.rendersSelect());

pessoa.update.addEventListener('click', () => pessoa.renderSelect());
