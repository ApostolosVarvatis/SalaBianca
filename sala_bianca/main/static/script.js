document.addEventListener("DOMContentLoaded", function () {

    // Responsive Menu Button
    const btn = document.getElementById("responsiveButton")
    const menu = document.getElementById("menu-wrap")
    const title = document.getElementById("title")

    btn.addEventListener('click', () => {
        btn.classList.toggle('open')
        menu.classList.toggle('open-menu')
        title.classList.toggle('fade')
        title.classList.toggle('unfade')
    })


    // Parallax Effect on navbars
    const parallax = document.querySelector(".scrollAnimation")

    window.addEventListener('scroll', function() {
        let offset = Math.floor(window.scrollY)
        parallax.style.backgroundPositionY = `${offset * 0.6}px`
    })


    // Parallax Effect on reservations
    const parallaxR = document.getElementById("reservations")

    window.addEventListener('scroll', function() {
        let offset = Math.floor(window.scrollY)
        parallaxR.style.backgroundPositionY = `${-550 + (offset * 0.7)}px`
    })

    // Parallax Effect on photoText
    const photoText = document.getElementById("photoText")

    window.addEventListener('scroll', function() {
        let offset = Math.floor(window.scrollY)
        if (offset >= 150) {
            photoText.classList.remove('opacity-0')
            photoText.classList.add('fadeInAndUp')
        }
    })
})


