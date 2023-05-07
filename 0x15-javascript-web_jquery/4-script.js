/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
$(function () {
  $('header').click(function () {
    $(this).toggleClass('red green');
  });
});
