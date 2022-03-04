/* WAD2 Team Project "Educ8" | "My Courses" Page Visual Scripts */

$(document).ready(function(){

  // Scripts for course tile elements
  $(".tile").each(function() {

    // Background color generator
    var red = Math.floor(Math.random() * 100) + 155;
    var green = Math.floor(Math.random() * 100) + 155;
    var blue = Math.floor(Math.random() * 100) + 155;
    $(this).css("background-color", `rgb(${red}, ${green}, ${blue})`);

    // Course title truncator
    if ($(this).find("h2").text().length > 32) {
      var text = $(this).find("h2").text();
      text = text.substr(0,32) + '...';
      $(this).find("h2").text(text);
    }

 });

});
