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

    // Fetch places and update the section
    $.ajax({
        type: 'POST',
        url: 'http://0.0.0.0:5001/api/v1/places_search/',
        data: JSON.stringify({}),
        contentType: 'application/json',
        success: function(data) {
            $('section.places').empty();
            for (let place of data) {
                $('section.places').append(
                    `<article>
                        <h2>${place.name}</h2>
                        <div class="price_by_night">$${place.price_by_night}</div>
                        <div class="information">
                            <div class="max_guest">${place.max_guest} Guests</div>
                            <div class="number_rooms">${place.number_rooms} Bedrooms</div>
                            <div class="number_bathrooms">${place.number_bathrooms} Bathrooms</div>
                        </div>
                    </article>`
                );
            }
        }
    });
});
