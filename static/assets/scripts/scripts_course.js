/* WAD2 Team Project "Educ8" | Course Page Visual Scripts */

$(document).ready(function(){

  $(".flashcard_tile").each(function() {

    // Generate background colour
    timGenerator($(this).find("h2").text(), $(this));

    // Course title truncator
    var text = $(this).find("p").text();
    if (text.length > 50) {
      text = text.substr(0,50) + '...';
      $(this).find("p").text(text);
    } else if (text.length < 40) {
      text += "<br>&nbsp;";
      $(this).find("p").html(text);
    }

  });

  // Remove colour from revise and add tiles
  $(".button_tile").each(function() {
    $(this).css("background-color", "white");
  });

});
