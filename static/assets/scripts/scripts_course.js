/* WAD2 Team Project "Educ8" | Course Page Visual Scripts */

$(document).ready(function(){

  $(".flashcard_tile").each(function() {

    // Generate background colour
    timGenerator($(this).find("h2").text(), $(this));

    // Flashcard question truncator
    var questionText = $(this).find("p").text();
    if (questionText.length > 50) {
      questionText = questionText.substr(0,50) + '...';
      $(this).find("p").text(questionText);
    } else if (questionText.length < 40) {
      questionText += "<br>&nbsp;";
      $(this).find("p").html(questionText);
    }

    // Flashcard title truncator
    var titleText = $(this).find("h2").text();
    if (titleText.length > 20) {
      titleText = titleText.substr(0,20) + '...';
      $(this).find("h2").text(titleText);
    }

  });

  // Remove colour from revise and add tiles
  $(".button_tile").each(function() {
    $(this).css("background-color", "white");
  });

});
