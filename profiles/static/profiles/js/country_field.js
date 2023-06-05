document.addEventListener("DOMContentLoaded", function () {
    let countrySelected = $('#id_default_country').val();

    if (!countrySelected) {
        $('#id_default_country').css('color', '#0d8065');
    } else {
        $('#id_default_country').css('color', '#3e3d3d').css('font-style', 'normal');
    }

    $('#id_default_country').change(function () {
        countrySelected = $(this).val();

        if (!countrySelected) {
            $(this).css('color', '#0d8065').css('font-style', 'italic');
        } else {
            $(this).css('color', '#3e3d3d').css('font-style', 'normal');
        }
    });
});
