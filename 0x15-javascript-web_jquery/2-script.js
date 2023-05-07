/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
$(document).ready(function () {
  $('#red_header').click(function () {
    $(this).css('color', 'red');
  });
});
