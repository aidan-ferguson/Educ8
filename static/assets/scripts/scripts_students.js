$(document).ready(function(){

    $("#add_student").click(function() {

        let student_to_add = $("#selection_field").find(":selected");
        let add_student_url = $("#selection_field").attr("add_student_url");
        $.ajax({
            url: add_student_url,
            data: {'student': student_to_add.attr("username")},
            success: function(data, status) {
                $("#current_students").append("<li>" + student_to_add.text() + "</li>")
                student_to_add.remove()
            },
            error: function(xhr, textStatus, errorText){
                if(xhr.status == 500){
                    $("#ajax_error").html(xhr.responseText);
                }
            }
        });  
    });

    $(".remove_student").click(function() {
        let student_to_remove = $(this).attr("student_username");
        let remove_student_url = $(this).attr("remove_student_url");
        $.ajax({
            url: remove_student_url,
            data: {'student': student_to_remove},
            success: function(data, status) {
                console.log($(this).parent()[0])
                $(this).parent()[0].remove();
                // TODO: add back to list
            },
            error: function(xhr, textStatus, errorText){
                if(xhr.status == 500){
                    $("#ajax_error").html(xhr.responseText);
                }
            }
        });  
    });
});