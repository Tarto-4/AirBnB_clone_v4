$(document).ready(function() {
    let amenities = {};

    // Listen for changes on each input checkbox
    $('input[type="checkbox"]').change(function() {
        if ($(this).is(":checked")) {
            // Store the Amenity ID and Name in the amenities object
            amenities[$(this).attr('data-id')] = $(this).attr('data-name');
        } else {
            // Remove the Amenity ID from the amenities object
            delete amenities[$(this).attr('data-id')];
        }

        // Update the h4 tag inside the div Amenities with the list of Amenities checked
        $('.amenities h4').text(Object.values(amenities).join(', '));
    });
});
