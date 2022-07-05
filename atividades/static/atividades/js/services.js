export async function getAreas() {
    let response = await fetch('/api/areas');
    return await response.json();
}

export async function getSubAreas() {
    let response = await fetch('/api/subareas/');
    return await response.json();
}

export async function getSubareasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/subareas/`);
    return await response.json();
}

export async function getPlataformasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/plataformas/`);
    return await response.json();
}

export async function getPessoasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/pessoas/`);
    return await response.json();
}

