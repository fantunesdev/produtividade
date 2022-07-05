export async function getAreas() {
    let response = await fetch('/api/areas');
    return await response.json();
}

export async function getSubAreas() {
    let response = await fetch('/api/subareas/');
    return await response.json();
}

export async function getSubAreasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/subareas/`);
    return await response.json();
}

