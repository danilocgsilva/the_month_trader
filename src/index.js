require('./styles.scss');

const burgetIcon = document.querySelector('.navbar-burger')
const navbarMenu = document.querySelector('.navbar-menu')

burgetIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active')
})
