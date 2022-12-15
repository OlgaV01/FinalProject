$('.back').hide();

$('.front', '.flashcard').hover(function() {
    $(this).hide();
    $(this).siblings('.back').addClass( "animated speed" ).show();
});

$('.back', '.flashcard').mouseleave(function() {
  $(this).hide();
  $('.front').addClass( "animated speed" ).show();
});
