/* WAD2 Team Project "Educ8" | "My Courses" Page Visual Scripts */

$(document).ready(function(){

  // Scripts for course tile elements
  $(".tile").each(function() {

    // Generate background colour
    timGenerator($(this).find("h2").text(), $(this));

    // Course title truncator
    if ($(this).find("h2").text().length > 32) {
      var text = $(this).find("h2").text();
      text = text.substr(0,32) + '...';
      $(this).find("h2").text(text);
    }


 });

});
