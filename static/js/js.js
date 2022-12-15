$('.back').hide();

$('.front', '.flashcard').hover(function() {
    $(this).hide();
    $(this).siblings('.back').addClass( "animate__flipInX speed" ).show();
});

$('.back', '.flashcard').mouseleave(function() {
  $(this).hide();
  $(this).siblings('.front').addClass( "animate__flipInX speed" ).show();
});