/* WAD2 Team Project "Educ8" | Flashcard Page Visual Scripts */

$(document).ready(function(){

  // Generate background colour
  timGenerator($(".card_panel").find("h2").text(), $(".card_panel"));

  // Toggle answers
  $("#toggle").click(function() {
    $("#question").toggle();
    $("#answer").toggle();
    $(this).find("span").text($(this).find("span").text() == 'Hide Answer' ? 'Reveal Answer' : 'Hide Answer');
  });

  // Next card
  $("#next").click(function() {
    
  });


});
