/* global $ */
// am adding $ as global since semistandard doest recognize and raises error
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append($('<li>item</li>'));
  });
});
