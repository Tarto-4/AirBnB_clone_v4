$(document).ready(function() {
    let selectedAmenities = {};

    // Listen for changes on each input checkbox tag
    $('input[type="checkbox"]').change(function() {
        if ($(this).is(":checked")) {
            selectedAmenities[$(this).attr('data-id')] = $(this).attr('data-name');
        } else {
            delete selectedAmenities[$(this).attr('data-id')];
        }
        
        // Update the h4 tag inside the div Amenities with the list of Amenities checked
        $('.amenities h4').text(Object.values(selectedAmenities).join(', '));
    });

    // Check the API status
    $.get('http://0.0.0.0:5001/api/v1/status/', function(data) {
        if (data.status === "OK") {
            $('#api_status').addClass('available');
        } else {
            $('#api_status').removeClass('available');
        }
    });
});
