import * as services from './services.js';
import * as components from './components.js';

const areaSelect = document.querySelector('#id_area'),
    areaUpdate = document.querySelector('#update-area'),
    subareaSelect = document.querySelector('#id_subarea'),
    subareaUpdate = document.querySelector('#update-subarea'),
    plataformaSelect = document.querySelector('#id_plataforma'),
    plataformaUpdate = document.querySelector('#update-plataforma'),
    pessoaSelect = document.querySelector('#id_pessoa'),
    pessoaUpdate = document.querySelector('#update-pessoa');


async function renderAreasSelect() {
    const areas = await services.getAreas();
    
    areaSelect.length = 0;
    components.renderOptions(areas, areaSelect.id);
}

async function renderSubareasSelect() {
    let areaId = areaSelect.selectedIndex;
    const subareas = await services.getSubareasArea(areaId);

    subareaSelect.length = 0;
    components.renderOptions(subareas, subareaSelect.id);
}

async function renderPlataformasSelect() {
    let areaId = areaSelect.selectedIndex;
    const plataformas = await services.getPlataformasArea(areaId);
    
    plataformaSelect.length = 0;
    components.renderOptions(plataformas, plataformaSelect.id);
}


async function renderPessoasSelect() {
    let areaId = areaSelect.selectedIndex;
    const pessoas = await services.getPessoasArea(areaId);

    pessoaSelect.length = 0;
    components.renderOptions(pessoas, pessoaSelect.id);
}


areaSelect.addEventListener('focusout', () => {
    renderSubareasSelect();
    renderPlataformasSelect();
    renderPessoasSelect();
});


areaUpdate.addEventListener('click', () => renderAreasSelect());


subareaUpdate.addEventListener('click', () => renderSubareasSelect());


plataformaUpdate.addEventListener('click', () => renderPlataformasSelect());


pessoaUpdate.addEventListener('click', () => renderPessoasSelect());
