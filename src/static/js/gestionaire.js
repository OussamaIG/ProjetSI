let more_main = document.querySelector('.main');
let more = document.querySelector('.more');
more.addEventListener('click',
    function() {
        more_main.classList.toggle('more');
    });

let more2 = document.querySelector('.more2');
more2.addEventListener('click',
    function() {
        more_main.classList.toggle('more2');
    });
let more3 = document.querySelector('.more3');
more3.addEventListener('click',
    function() {
        more_main.classList.toggle('more3');
    });

let listm = document.querySelectorAll('.navigation ul li');

function activateLink() {
    listm.forEach((item) =>
        item.classList.remove('hovered'));
    this.classList.add('hovered');
}
listm.forEach((item) =>
    item.addEventListener('mouseover', activateLink));

let togglem = document.querySelector('.toggle');
let navigationm = document.querySelector('.navigation');

togglem.addEventListener('click',
    function() {
        navigationm.classList.toggle('active');
        more_main.classList.toggle('active');
    });