/* WAD2 Team Project "Educ8" | "My Courses" Page Visual Scripts */

$(document).ready(function(){

  // Scripts for course tile element
  $(".tile").each(function() {

    // Generate background colour
    timGenerator($(this).find("h2").text(), $(this));

    // Course title truncator
    var text = $(this).find("h2").text();
    if (text.length > 32) {
      text = text.substr(0,32) + '...';
      $(this).find("h2").text(text);
    } else if (text.length < 22) {
      text += "<br>&nbsp;";
      $(this).find("h2").html(text);
    }


 });

 // Remove colour from create course tile
 $(".create_tile").each(function() {
   $(this).css("background-color", "white");
 });

});
