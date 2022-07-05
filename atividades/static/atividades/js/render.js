import * as services from './services.js';
import * as components from './components.js';

const areaSelect = document.querySelector('#id_area'),
    areaUpdate = document.querySelector('#update-area'),
    subareaSelect = document.querySelector('#id_subarea'),
    subareaUpdate = document.querySelector('#update-subarea');


async function renderAreasSelect() {
    const areas = await services.getAreas();
    
    areaSelect.length = 0;
    components.renderOptions(areas, areaSelect.id);
}

async function renderSubareasSelect() {
    let areaId = areaSelect.selectedIndex;
    const subareas = await services.getSubAreasArea(areaId);

    subareaSelect.length = 0;
    components.renderOptions(subareas, subareaSelect.id);
}


areaSelect.addEventListener('focusout', () => {
    renderSubareasSelect();
});

areaUpdate.addEventListener('click', () => {
    renderAreasSelect();
});

subareaUpdate.addEventListener('click', () => {
    renderSubareasSelect();
});