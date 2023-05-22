document.addEventListener("DOMContentLoaded", function () {
    /**
    * Handles the image change on product
    */
    $('#new-image').change(function () {
        var file = $('#new-image')[0].files[0];
        $('#filename').text(`Image will be set to: ${file.name}`);
    });
});