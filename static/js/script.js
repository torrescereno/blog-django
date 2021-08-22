const hamburger = document.querySelector(".nav__hamburger");
const navMenu = document.querySelector(".nav__menu")
const navLink = document.querySelectorAll(".nav__link");

hamburger.addEventListener("click", mobileMenu)
navLink.forEach(n => n.addEventListener("click", closeMenu));

function mobileMenu() {
    hamburger.classList.toggle("active")
    navMenu.classList.toggle("active")
}

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}