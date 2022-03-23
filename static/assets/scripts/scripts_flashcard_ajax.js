/* WAD2 Team Project "Educ8" | Flashcard Page AJAX Scripts */

$(document).ready(function(){

  $("#next").click(function() {

    var courseIdVar = $(this).attr("data-courseId");
    $.get(
      '/Educ8/next_card/', {'courseId': courseIdVar, 'current_flashcard_num': $("#next").attr("data-flashcard-num")},
      function(data) {
        $("#title").html(JSON.parse(data)["titleText"]);
        $("#question").html(JSON.parse(data)["questionText"]);
        $("#answer").html(JSON.parse(data)["answerText"]);
        $("#next").attr("data-flashcard-num", JSON.parse(data)["new_flashcard_num"])

        if ($("#question:visible").length==0) {
          $("#toggle").trigger("click");
        }
        timGenerator($(".card_panel").find("h2").text(), $(".card_panel"));

      });

  });

  $("#next").trigger("click");

});
