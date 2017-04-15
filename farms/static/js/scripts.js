// this is a scripts file

$(document).ready(function() {

//    $('#button-id-complete').click(function() {
    $('#id_postal_code').keyup(function() {

        var postal_code = $("#id_postal_code").val()

        if(postal_code.length > 3){

            $.ajax({
                url: "get_places",
                data: {
                  postal_code: postal_code
                },
                type: "GET",
                dataType: "json",
            })
              .done(function( json ) {
//                http://stackoverflow.com/a/14447147
//                 $( "#id_place").val( json.place );
                 $('#id_place')
                    .empty()
                    .append($('<option>', {
                        value: json.place,
                        text: json.place + ', ' + json.municipality + ', ' + json.city
                }));
                 $( "#id_municipality").val( json.municipality );
                 $( "#id_city").val( json.city );
                 $( "#id_state").val( json.state );
              })
         }
          // Code to run if the request fails; the raw request and
          // status codes are passed to the function
//          .fail(function( xhr, status, errorThrown ) {
//            alert( "Sorry, there was a problem!" );
//            console.log( "Error: " + errorThrown );
//            console.log( "Status: " + status );
//            console.dir( xhr );
//          })
    });
});