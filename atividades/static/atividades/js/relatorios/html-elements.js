export function renderBox(father, htmlId) {
    const box = document.createElement('div');
    
    box.classList.add('box');
    box.classList.add('box-primary', 'box-max-width-920px', 'center-div');
    box.id = htmlId;

    father.appendChild(box);
    
    for (let i = 0; i < 3; i++) {
        let boxSection = document.createElement('div');
        
        switch (i) {
            case 0:
                boxSection.classList.add('box-title');
                break;
            case 1:
                boxSection.classList.add('box-body');
                break;
            case 2:
                boxSection.classList.add('box-footer');
                break;
        }
        box.appendChild(boxSection);
    }
    return box;
}

export function renderBoxTitle(father, title) {
    const boxTitle = document.createElement('div'),
        h3 = document.createElement('h3');
    
    boxTitle.classList.add('box-title');
    h3.innerHTML = title;
    father.appendChild(h3);
    return boxTitle;
}

export function renderBoxBody(father, activities) {
    const boxBody = document.createElement('div');
    for (let activity of activities) {
        const p = document.createElement('p');
        p.innerHTML = `${activity.data} - ${activity.descricao}`;
        boxBody.appendChild(p);
    }
    father.appendChild(boxBody);
    return boxBody;

}

export function renderBoxFooter(father, activities) {
    const boxFooter = document.createElement('div'),
        span = document.createElement('span');

    span.innerHTML = `Total: ${activities.length}.`
    father.appendChild(span);
}