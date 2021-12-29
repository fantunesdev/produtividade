var mm = 0;
var ss = 0;
var status = 1;

var tempo = 1000;
var cron;

function start(){
    if(status == 1){
        cron = setInterval(() => { timer(); }, tempo);
        status = 0;
        document.getElementById('start').innerText = 'Parar'
    } else {
        clearInterval(cron);
        status = 1;
        document.getElementById('start').innerText = 'Retomar'
    }

}

function registrar(){
    if(document.getElementById('id_tempo').value == ''){
        if(ss < 10){
            document.getElementById('id_tempo').value = mm;
        } else {
            document.getElementById('id_tempo').value = mm + 1;
        }
        zerar()
    } else {
        if(ss < 10){
            document.getElementById('id_tempo').value = parseInt(document.getElementById('id_tempo').value) + mm;
        } else {
            document.getElementById('id_tempo').value = parseInt(document.getElementById('id_tempo').value) + mm + 1;
        }
        zerar()
    }
}

function plus(){
    mm = mm + 1

    var format = (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
    document.getElementById('counter').innerText = format;
}

function minus(){
    if(mm > 0){
        mm = mm - 1

        var format = (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
        document.getElementById('counter').innerText = format;
    }
}

function zerar(){
    clearInterval(cron);
    mm = 0;
    ss = 0;
    status = 1;

    document.getElementById('counter').innerText = '00:00';
    document.getElementById('start').innerText = 'Iniciar'
}

function timer(){
    ss++;
    if(ss == 60){
        ss = 0;
        mm++;
    }

    var format = (mm < 10 ? '0' + mm : mm) + ':' + (ss < 10 ? '0' + ss : ss);
    document.getElementById('counter').innerText = format;
}
