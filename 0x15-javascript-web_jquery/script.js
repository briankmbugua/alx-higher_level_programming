console.log('Welcome to the ultimate jQuery course');
// $('.p1').click(function(){
//   $(this).hide();
// })

// $('#p2').mouseenter(function(){
//   $(this).css({
//     'color':'red',
//     'font-size':'50px'
//   })
// });

// $('#p2').mouseleave(function(){
//   $(this).css({
//     'color':'inherit',
//     'font-size':'inherit'
//   })
// });

// $('.p1').hover(function(){
//   $(this).css({
//     'color':'red',
//     'font-size':'50px'
//   }),
//   function() {
//     $(this).css({
//       'color':'inherit',
//       'font-size':'inherit'
//     })
//   }
// })

// $('.p1').hover(function(){
//   $(this).css({
//     'color':'red',
//     'font-size':'30px'
//   })
// },
// function() {
//   $(this).css({
//     'color':'green',
//     'font-size':'10px'
//   })
// });

// $('input').focus(function(){
//   $(this).css('background-color','#cccccc',
//   );
// });
// $('input').blur(function(){
//   $(this).css('background-color','#ffffff');
// });

$('.p1').on(
  {
    mouseenter: function () {
      $(this).css('background-color', 'green');
    },
    mouseleave: function () {
      $(this).css('background-color', 'inherit');
    },
    click: function () {
      $(this).css({
        border: '20px solid green',
        padding: '20px',
        color: 'green'
      });
    }
  }
);

$('button').click(function () {
  $('.p1').hide(1000);
});
