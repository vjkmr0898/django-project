    // hinging the message
$(document).ready(function(){
  $('.alert').hide(4000);
});

    
    
// get the select, quantity, price, and total tags
var select = document.getElementById('product');
var quantity = document.getElementById('quantity');
var price = document.getElementById('price');
var total = document.getElementById('total');

// add an event listener to the select and quantity tags
select.addEventListener('change', updatePrice);
quantity.addEventListener('input', updatePrice);

function updatePrice() {
  // get the selected option value and price, and the user's entered quantity
    var product = select.value;
    var priceValue = select.options[select.selectedIndex].dataset.price;
    var quantityValue = quantity.value;
    
  // calculate the total cost based on the selected product's price and the user's entered quantity
  var totalValue = (priceValue * quantityValue).toFixed(2);
    
  // set the value of the price and total input tags
    price.value = priceValue;
    total.value = totalValue;
}