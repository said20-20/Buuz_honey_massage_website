// Navigation Toggle
const burger = document.querySelector('.burger');
const navLinks = document.querySelector('.nav-links');
const nav = document.querySelector('nav');

burger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    burger.classList.toggle('active');
});

// Change Navbar on Scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});
