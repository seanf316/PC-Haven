document.addEventListener("DOMContentLoaded", function () {
    /**
    * Handles the site toasts
    */
    let toast = $('.toast');
    let hideTimeout;

    toast.toast('show');

    toast.on('mouseenter touchstart', function () {
        $(this).toast('show');
        clearTimeout(hideTimeout);
    });

    hideTimeout = setTimeout(function () {
        toast.toast('hide');
    }, 3000);

    toast.on('mouseleave touchend', function () {
        hideTimeout = setTimeout(function () {
            toast.toast('hide');
        }, 3000);
    });

    function hideToastOnScroll() {
        toast.toast('hide');
        clearTimeout(hideTimeout);
    }

    window.addEventListener('scroll', hideToastOnScroll);

});
