/* WAD2 Team Project "Educ8" | Flashcard Page AJAX Scripts */

$(document).ready(function(){

  $("#next").click(function() {

    var courseIdVar = $(this).attr("data-courseId");
    $.get(
      '/Educ8/next_card/', {'courseId': courseIdVar},
      function(data) {
        $("#title").html(JSON.parse(data)["titleText"]);
        $("#question").html(JSON.parse(data)["questionText"]);
        $("#answer").html(JSON.parse(data)["answerText"]);
        if ($("#question:visible").length==0) {
          $("#toggle").trigger("click");
        }
        timGenerator($(".card_panel").find("h2").text(), $(".card_panel"));

      });

  });

  $("#next").trigger("click");

});
