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

export async function updateArea(area, csrf) {
    const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
    requestOptions = {
        method: "PUT",
        headers: headers,
        body: area
        };
    const areaJson = JSON.parse(area);
    let response = await fetch(`/api/areas/${areaJson.id}/`, requestOptions);
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

export async function getSubareaId(subarea_id) {
    let response = await fetch(`/api/subareas/${subarea_id}/`)
    return await response.json();
}

export async function updateSubarea(subarea, csrf) {
    const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
    requestOptions = {
        method: "PUT",
        headers: headers,
        body: subarea
        };
    const subareaJson = JSON.parse(subarea);
    let response = await fetch(`/api/subareas/${subareaJson.id}/`, requestOptions);
    return await response.json();
}


export async function createPlataforma(plataforma, csrf) {
    const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
        requestOptions = {
            "method": "POST",
            "headers": headers,
            "body": plataforma
        };

    const response = await fetch(`/api/plataformas/`, requestOptions);
    return await response.json();
}

export async function getPlataformasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/plataformas/`);
    return await response.json();
}

export async function getPlataformaId(platforma_id) {
    const response = await fetch(`/api/plataformas/${platforma_id}/`);
    return await response.json();
}

export async function updatePlataforma(plataforma, csrf) {
    const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
        requestOptions = {
            "method": "PUT",
            "headers": headers,
            "body": plataforma
        };

    const plataformaJson = JSON.parse(plataforma),
        response = await fetch(`/api/plataformas/${plataformaJson.id}/`, requestOptions);
        return await response.json();
}


export async function createPessoa(pessoa, csrf) {
    const headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf
        },
        requestOptions = {
            "method": "POST",
            "headers": headers,
            "body": pessoa
        };

    const response = await fetch('/api/pessoas/', requestOptions);
    return await response.json();

}

export async function getPessoaId(pessoa_id) {
    const response = await fetch(`/api/pessoas/${pessoa_id}`);
    return await response.json();
}

export async function getPessoasArea(areaId) {
    let response = await fetch(`/api/areas/${areaId}/pessoas/`);
    return await response.json();
}

export async function updatePessoa(pessoa, csrf) {
    const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
        requestOptions = {
            "method": "PUT",
            "headers": headers,
            "body": pessoa
        };
    const pessoaJson = JSON.parse(pessoa),
        response = await fetch(`/api/pessoas/${pessoaJson.id}/`, requestOptions);
    return await response.json();
}
