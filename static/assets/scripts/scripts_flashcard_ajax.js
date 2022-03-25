/* WAD2 Team Project "Educ8" | Flashcard Page AJAX Scripts */

$(document).ready(function(){

  function next_card(button) {

    let next_card_url = $("#card_panel").attr("next_card_url");
    $.get(next_card_url, {'current_flashcard_num': $("#card_panel").attr("data-flashcard-num")},
      function(data) {
        console.log(data)
        $("#title").html(JSON.parse(data)["titleText"]);
        $("#question").html(JSON.parse(data)["questionText"]);
        $("#answer").html(JSON.parse(data)["answerText"]);
        $("#card_panel").attr("data-flashcard-num", JSON.parse(data)["new_flashcard_num"])


        if ($("#question:visible").length==0) {
          $("#toggle").trigger("click");
        }
        timGenerator($(".card_panel").find("h2").text(), $(".card_panel"));

      });

  }

  $("#next").click(next_card);

  next_card();

});
