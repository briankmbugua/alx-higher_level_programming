/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
console.log('from jquery');
$(document).ready(function () {
  $('#red_header').click(function () {
    $(this).addClass('red');
  });
});
