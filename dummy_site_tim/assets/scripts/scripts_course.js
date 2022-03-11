/* WAD2 Team Project "Educ8" | Course Page Visual Scripts */

$(document).ready(function(){

  $(".flashcard_tile").each(function() {

    // Generate background colour
    timGenerator($(this).find("h2").text(), $(this));

  });

  // Remove colour from revise and add tiles
  $(".button_tile").each(function() {
    $(this).css("background-color", "white");
  });

});
