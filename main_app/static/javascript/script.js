// import 'bootstrap-icons/font/bootstrap-icons.css';

let navBar = document.getElementById('navBar');
let navBarNav = document.getElementById('navbarNav');
let navLinks = navBarNav.querySelectorAll('a.nav-link, button.btn-link');
let navbarUl = document.getElementById('navbarUl');
let navbarUlLinks = navBarNav.querySelectorAll('li.nav-item , button.btn-link')
let yAxisTop = navBar.offsetTop;

window.addEventListener('scroll', function() {
    if(window.scrollY > 50) {
        navBar.classList.add('scrolled');
        navbarUlLinks.forEach(function(link) {
            link.classList.add('navbarUlColor');
        });

        
        navLinks.forEach(function(link) {
            link.classList.add('linkColor');
        });
    }
    else {
        navBar.classList.remove('scrolled');
        
        navbarUlLinks.forEach(function(link) {
            link.classList.remove('navbarUlColor');
        });

        navLinks.forEach(function(link) {
            link.classList.remove('linkColor');
        });


    }
})