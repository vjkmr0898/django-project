// hinging the message
$(document).ready(function(){
    $('.alert').hide(4000);
});


// adding items
$(document).ready(function(){
    $("#add_product").click(function(){
        $("#model_product").modal();
    });
});
// updating item
$(document).ready(function() {

$('.edit').click(function() {
$("#my-modal").modal()
var id = $(this).closest('tr').data('id');
$.ajax({
    url: '/get_row_data/' + id +'/',
    dataType: 'json',
    method:'GET',
    cache:false,
    success: function(data) 
    {
        // alert(data);
    
    $('#id').val(data.id);
    $('#product_name').val(data.product_name);
    $('#units').val(data.unit);
    $('#available_items').val(data.available_items);
    // alert(data.available_items);
    $('#price_per_unit').val(data.price);
    // alert(data.price);
    
    },
    error: function(xhr, status, error) {
    
    }
});
});
});
