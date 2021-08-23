const hamburger = document.querySelector(".nav__hamburger");
const navMenu = document.querySelector(".nav__menu")
const navLink = document.querySelectorAll(".nav__link");

function funTogle() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

hamburger.addEventListener("click", funTogle)

navLink.forEach(n => n.addEventListener("click", funTogle));