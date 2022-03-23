$(document).ready(function(){

    $("#add_student").click(function() {
        
      let student_to_add = $("#selection_field").find(":selected");
      let add_student_url = $("#selection_field").attr("add_student_url");
      $.get(add_student_url, {'student': student_to_add.attr("username")},
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
  