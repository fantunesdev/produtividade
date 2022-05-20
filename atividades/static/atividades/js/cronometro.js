// Counter Logic Variables
let counter,
    time = 1000,
    mm = 0,
    ss = 0,
    counterIsRunning = false;

// HTML Elements
let counterDisplay = document.getElementById('counter-display'),
    startButton = document.getElementById('start-button'),
    timeInput = document.getElementById('id_tempo');

function timer(){
    ss++;
    if(ss === 60){
        ss = 0;
        mm++;
    }

    let format = `${(mm < 10 ? `0${mm}` : mm)}:${(ss < 10 ? `0${ss}` : ss)}`;
    counterDisplay.innerHTML = format;
}

function runCounter() {
    if(counterIsRunning) {
        clearInterval(counter);
        counterIsRunning = false;
        startButton.value = 'Retomar';
    } else {
        counter = setInterval(() => timer(), time);
        counterIsRunning = true;
        startButton.value = 'Parar';
    }

}

function resetCounter(){
    clearInterval(counter);
    mm = 0;
    ss = 0;
    counterIsRunning = false;

    counterDisplay.innerHTML = '00:00';
    startButton.value = 'Iniciar'
}

function addMinute(){
    mm++;
    let format = `${(mm < 10 ? `0${mm}` : mm)}:${(ss < 10 ? `0${ss}` : ss)}`;
    counterDisplay.innerHTML = format;
}

function subtractMinute(){
    if(mm > 0){
        mm--;
        let format = `${(mm < 10 ? `0${mm}` : mm)}:${(ss < 10 ? `0${ss}` : ss)}`;
        counterDisplay.innerHTML = format;
    }
}

function registerOnInput(){
    if(timeInput.value == ''){
        ss < 10 ? timeInput.value = mm : timeInput.value = mm + 1;
        resetCounter()
    } else {
        if(ss < 10){
            timeInput.value = parseInt(timeInput.value) + mm;
        } else {
            timeInput.value = parseInt(timeInput.value) + mm + 1;
        }
        resetCounter()
    }
}
