/* WAD2 Team Project "Educ8" | Flashcard Page AJAX Scripts */

$(document).ready(function(){

  $("#next").click(function() {

    let next_card_url = $(this).attr("next_card_url");
    $.get(next_card_url, {'current_flashcard_num': $("#next").attr("data-flashcard-num")},
      function(data) {
        $("#title").html(JSON.parse(data)["titleText"]);
        $("#question").html(JSON.parse(data)["questionText"]);
        $("#answer").html(JSON.parse(data)["answerText"]);
        $("#next").attr("data-flashcard-num", JSON.parse(data)["new_flashcard_num"])

        console.log(data)
        if ($("#question:visible").length==0) {
          $("#toggle").trigger("click");
        }
        timGenerator($(".card_panel").find("h2").text(), $(".card_panel"));

      });

  });

  $("#next").trigger("click");

});
