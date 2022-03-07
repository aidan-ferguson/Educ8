/* WAD2 Team Project "Educ8" | Course Page Visual Scripts */

$(document).ready(function(){

  $(".flashcard_tile").each(function() {

    // Background color generator
    var red = Math.floor(Math.random() * 100) + 155;
    var green = Math.floor(Math.random() * 100) + 155;
    var blue = Math.floor(Math.random() * 100) + 155;
    $(this).css("background-color", `rgb(${red}, ${green}, ${blue})`);

  });

});
