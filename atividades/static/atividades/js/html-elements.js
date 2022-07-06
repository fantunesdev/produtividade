

export function renderOptions(objectList, htmlId) {
    const input = document.querySelector(`#${htmlId}`);
    let option,
        item;

    for (item of objectList) {
        option = document.createElement('option');
        option.value = item.id;
        option.text = item.nome;
        input.add(option, input.options[item.id]);
    }
    input.value = 0;
}

export function renderDefaultOption(htmlId) {
    const input = document.querySelector(`#${htmlId}`);
    let option;

    option = document.createElement('option');
    option.value = 0;
    option.text = '---------';
    input.add(option, input.options[0]);
}