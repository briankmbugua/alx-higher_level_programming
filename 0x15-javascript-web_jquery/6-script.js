/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
$(document).ready(function () {
  $('#update_header').click(function () {
    const header = $('header');
    header.text('New text content');
  });
});
