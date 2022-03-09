/* WAD2 Team Project "Educ8" | Flashcard Page Visual Scripts */

$(document).ready(function(){

  // Background color generator
  var red = Math.floor(Math.random() * 100) + 155;
  var green = Math.floor(Math.random() * 100) + 155;
  var blue = Math.floor(Math.random() * 100) + 155;
  $(".card_panel").css("background-color", `rgb(${red}, ${green}, ${blue})`);

});
