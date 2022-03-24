$(document).ready(function(){

    $("#add_student").click(function() {

        let student_to_add = $("#selection_field").find(":selected");
        let add_student_url = $("#selection_field").attr("add_student_url");
        $.ajax({
            url: add_student_url,
            data: {'student': student_to_add.attr("value")},
            success: function(data, status) {
                let bin_button = '<i class="fa fa-trash-can remove_student" student_username="' + student_to_add.attr("value") +'"></i>'
                let new_entry = $("#current_students").append("<li><p>" + student_to_add.text() + bin_button + "</p></li>")
                new_entry.find("p").find("i").click(remove_student);
                student_to_add.remove()
            },
            error: function(xhr, textStatus, errorText){
                if(xhr.status == 500){
                    $("#ajax_error").html(xhr.responseText);
                }
            }
        });  
    });

    function remove_student(button) {
        let clicked_element = $(this);
        let remove_student_url = $(this).parent().parent().parent().attr("remove_student_url");
        
        $.ajax({
            url: remove_student_url,
            data: {'student': clicked_element.attr("student_username")},
            success: function(data, status) {
                $("#selection_field").append($('<option>',{
                    value: clicked_element.attr("student_username"),
                    text: clicked_element.parent().text(),
                }));
                clicked_element.parent().parent().remove();
            },
            error: function(xhr, textStatus, errorText){
                if(xhr.status == 500){
                    $("#ajax_error").html(xhr.responseText);
                }
            }
        });
    }

    $(".remove_student").click(remove_student);  
    
});