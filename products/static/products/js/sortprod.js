document.addEventListener("DOMContentLoaded", function () {
    /**
     * Changes the sort choice on product sort selector
     * Sets the sort value and direction value by splitting at the '_'
     * Checks if sort choice is equal to 'sub_category' and handles the sort differently
     */
    $('#sort-selector').change(function () {

        const sortChoice = $(this).val();
        const currentUrl = new URL(window.location);

        if (sortChoice != "reset" && sortChoice != 'sub_category_asc' && sortChoice != 'sub_category_desc') {
            let sort = sortChoice.split("_")[0];
            let direction = sortChoice.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else if (sortChoice == "sub_category_asc") {
            let sort = 'sub_category';
            let direction = 'asc';

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else if (sortChoice == "sub_category_desc") {
            let sort = 'sub_category';
            let direction = 'desc';

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });
});