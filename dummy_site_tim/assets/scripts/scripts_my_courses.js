/* WAD2 Team Project "Educ8" | "My Courses" Page Visual Scripts */

$(document).ready(function(){

  // Set each course tile background colour
  $(".tile").each(function() {
    var red = Math.floor(Math.random() * 100) + 155;
    var green = Math.floor(Math.random() * 100) + 155;
    var blue = Math.floor(Math.random() * 100) + 155;
    $(this).css("background-color", `rgb(${red}, ${green}, ${blue})`);
 });

});
