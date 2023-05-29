document.addEventListener("DOMContentLoaded", function () {

    let toast = $('.toast');

    toast.toast('show');

    toast.on('mouseenter', function () {
        $(this).toast('show');
        clearTimeout(hideTimeout);
    });

    let hideTimeout = setTimeout(function () {
        toast.toast('hide');
    }, 3000);

    toast.on('mouseleave', function () {
        hideTimeout = setTimeout(function () {
            toast.toast('hide');
        }, 3000);
    });

});