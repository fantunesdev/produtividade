export async function createArea(area, csrf) {
    const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf
        },
        requestOptions = {
            method: "POST",
            headers: headers,
            body: area,
        };
    let response = await fetch('/api/areas/', requestOptions),
        data = await response.json();
    console.log(data.headers);
    return data;
}

export async function getAreas() {
    let response = await fetch('/api/areas/');
    return await response.json();
}

export async function getAreaId(id) {
    let response = await fetch(`/api/areas/${id}/`)
    return await response.json();
}


export async function createSubarea(subarea, csrf) {
    const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf
        },
        requestOptions = {
            method: "POST",
            headers: headers,
            body: subarea,
        };
    const response = await fetch('/api/subareas/', requestOptions);
    
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

