let areas = document.querySelector('#id_area'),
    subAreas = document.querySelector('#id_sub_area');
   
function getSubAreas(area) {
    let url = `/api/areas/${area}/sub_areas/`,
        subAreaOption,
        i;

    fetch(url)
        .then(response => response.json())
        .then(dados => {
            subAreas.length = 0;
            for(i = 0; i < dados.length; i++){
                subAreaOption = document.createElement('option');
                subAreaOption.value = dados[i].id;
                subAreaOption.text = dados[i].nome;
                subAreas.add(subAreaOption, subAreas.options[i]);
            }
            subAreas.value = null;
        });
}

areas.addEventListener('focusout', function(){
    getSubAreas(areas.value);
});