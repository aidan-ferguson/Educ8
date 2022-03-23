$(document).ready(function(){

    $("#add_student").click(function() {
  
      let student_to_add = $("#selection_field").find(":selected");
      $.get('add_student/', {'student': student_to_add.attr("username")},
        function(data, status) {
            if(status === "success"){
                $("#current_students").append("<li>" + student_to_add.text() + "</li>")
                student_to_add.remove()
            } else {
                $("ajax_error").html(data);
            }
        });
  
    });  
});
  