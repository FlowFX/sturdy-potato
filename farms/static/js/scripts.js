// this is a scripts file

$(document).ready(function() {

    $('#button-id-complete').click(function() {

        $.get('/farms/addresses/get_places', {postal_code: '06760'});

//        #, function(data){

//            $('#id_city').html(data);
//            $('#id_city').hide();

        });

    });
//    }
//    $('#likes').click(function(){
//    var catid;
//    catid = $(this).attr("data-catid");
//     $.get('/rango/like_category/', {category_id: catid}, function(data){
//               $('#like_count').html(data);
//               $('#likes').hide();
//           });



});