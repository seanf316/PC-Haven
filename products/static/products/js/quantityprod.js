document.addEventListener("DOMContentLoaded", function () {
    /**
     * Check current value of quantity input
     * sets min and max values
     * disables buttons when exceeded
     * sets value to stock limit if keyboard used to enter value greater than stock limit
     */
    function handleEnableDisable(productId) {
        let qtyInput = $(`#id_qty_${productId}`);
        let qtyInputValue = parseInt(qtyInput.val());
        let qtyMax = parseInt(qtyInput.attr('max'));
        var minusDisabled = qtyInputValue < 2;
        var plusDisabled = qtyInputValue >= qtyMax;
        $(`#decrement-qty_${productId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${productId}`).prop('disabled', plusDisabled);
        if (qtyInputValue > qtyMax) {
            qtyInput.val(qtyMax);
        } else if (qtyInputValue < 1) {
            qtyInput.val(1);
        }
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for (var i = 0; i < allQtyInputs.length; i++) {
        var productId = $(allQtyInputs[i]).data('product_id');
        handleEnableDisable(productId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function () {
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
    });

    // Increment quantity
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
    });
});
