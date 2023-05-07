/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
console.log('jquery');
$(document).ready(function () {
  $('header').css('background-color', '#FF0000');
});
