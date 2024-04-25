let targetDate = new Date("2026-12-01T23:59:59");
let countdownInterval;

function startCountdown() {
    countdownInterval = setInterval(updateCountdown, 1000);
}

function updateCountdown() {
    let currentDate = new Date();
    let timeDifference = targetDate - currentDate;

    if (timeDifference <= 0) {
        clearInterval(countdownInterval);
        document.getElementById("days").innerText = "00";
        document.getElementById("hours").innerText = "00";
        document.getElementById("minutes").innerText = "00";
        document.getElementById("seconds").innerText = "00";
    } else {
        let days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        let hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = padLeft(days);
        document.getElementById("hours").innerText = padLeft(hours);
        document.getElementById("minutes").innerText = padLeft(minutes);
        document.getElementById("seconds").innerText = padLeft(seconds);
    }
}

function padLeft(value) {
  return value < 10 ? "0" + value : value;
}


// Inicia el cronómetro cuando la página se carga
window.onload = startCountdown;
