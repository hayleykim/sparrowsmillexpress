let navBar = document.getElementById('navBar');
let navBarNav = document.getElementById('navbarNav');
let yAxisTop = navBar.offsetTop;

window.addEventListener('scroll', function() {
    if(window.scrollY > 50) {
        navBar.classList.add('scrolled');

        let navLinks = navBarNav.querySelectorAll('a.nav-link, button.btn-link');
        navLinks.forEach(function(link) {
            link.classList.add('linkColor');
        });
    }
    else {
        navBar.classList.remove('scrolled');
        
        let navLinks = navBarNav.querySelectorAll('a.nav-link, button.btn-link');
        navLinks.forEach(function(link) {
            link.classList.remove('linkColor');
        });


    }
})