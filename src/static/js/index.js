let list1 = document.querySelectorAll('.navigation ul li');

function activateLink() {
    list1.forEach((item) =>
        item.classList.remove('hovered'));
    this.classList.add('hovered');
}
list1.forEach((item) =>
    item.addEventListener('mouseover', activateLink));

let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main');

toggle.addEventListener('click',
    function() {
        navigation.classList.toggle('active');
        main.classList.toggle('active');
    });