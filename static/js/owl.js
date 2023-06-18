document.addEventListener("DOMContentLoaded", function () {

    // Owl Carousel 
    $('.owl-carousel').owlCarousel({
        loop: false,
        margin: 15,
        dots: false,
        nav: true,
        responsive: {
            0: {
                items: 1,
                dots: false,
                loop: true,
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    })
})