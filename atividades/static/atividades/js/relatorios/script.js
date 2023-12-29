import * as services from './services.js';
import * as htmlElements from './html-elements.js';

const main = document.querySelector('main'),
    teste = document.querySelector('#btn-teste'),
    monthsTable = {
        1: {
                por: "Janeiro",
                ing: "January"
            },
        2: {
                por: "Fevereiro",
                ing: "February"
            },
        3: {
                por: "Março",
                ing: "March"
            },
        4: {
                por: "Abril",
                ing: "April"
            },
        5: {
                por: "Maio",
                ing: "May"
            },
        6: {
                por: "Junho",
                ing: "June"
            },
        7: {
                por: "Julho",
                ing: "July"
            },
        8: {
                por: "Agosto",
                ing: "August"
            },
        9: {
                por: "Setembro",
                ing: "September"
            },
        10: {
            por: "Outubro",
            ing: "October"
        },
        11: {
            por: "Novembro",
            ing: "November"
        },
        12: {
            por: "Dezembro",
            ing: "December"
        }
    };





(async function createBoxes() {
    const activitiesByMonth = await groupByMonth();
    for (let i = 1; i <= 12; i++) {
        if (activitiesByMonth[i].length !== 0) {
            const box = htmlElements.renderBox(main, `activities-${monthsTable[i].ing.toLowerCase()}`),
                boxTitle = box.children[0],
                boxBody = box.children[1],
                boxFooter = box.children[2];
    
            htmlElements.renderBoxTitle(boxTitle, `Atividades de ${monthsTable[i].por}`);
            htmlElements.renderBoxBody(boxBody, activitiesByMonth[i]);
            htmlElements.renderBoxFooter(boxFooter, activitiesByMonth[i]);
        }
    }
})()

async function groupByMonth() {
    const activities = await services.getAtividadesAno(2022);
    let monthGroup = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
    }

    for (let activity of activities) {
        const [year, month, day] = activity.data.split('-');
        switch (month) {
            case '01':
                monthGroup[1].push(activity);
                break;
            case '02':
                monthGroup[2].push(activity);
                break;
            case '03':
                monthGroup[3].push(activity);
                break;
            case '04':
                monthGroup[4].push(activity);
                break;
            case '05':
                monthGroup[5].push(activity);
                break;
            case '06':
                monthGroup[6].push(activity);
                break;
            case '07':
                monthGroup[7].push(activity);
                break;
            case '08':
                monthGroup[8].push(activity);
                break;
            case '09':
                monthGroup[9].push(activity);
                break;
            case '10':
                monthGroup[10].push(activity);
                break;
            case '11':
                monthGroup[11].push(activity);
                break;
            case '12':
                monthGroup[12].push(activity);
                break;
        
            default:
                break;
        }
    }
    return monthGroup;
}
