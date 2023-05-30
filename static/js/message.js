document.addEventListener("DOMContentLoaded", function () {

    let toast = $('.toast');

    toast.toast('show');

    toast.on('mouseenter touchstart', function () {
        $(this).toast('show');
        clearTimeout(hideTimeout);
    });

    let hideTimeout = setTimeout(function () {
        toast.toast('hide');
    }, 3000);

    toast.on('mouseleave touchend', function () {
        hideTimeout = setTimeout(function () {
            toast.toast('hide');
        }, 3000);
    });

});