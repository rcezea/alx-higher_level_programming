$(function () {
  $('DIV#add_item').on('click', function () {
    const add = $('<li>Item</li>');
    $('UL.my_list').append(add);
  });
});
