$(document).ready(function(){

    $("#add_student").click(function() {
  
      let student_to_add = $("#selection_field").find(":selected").attr("username");
      $.get('add_student/', {'student': student_to_add},
        function(data, status) {
            if(status !== "success"){
                $("ajax_error").html(data);
            }
        });
  
    });  
});
  