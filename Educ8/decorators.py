def student_required(user):
    return user.is_active and user.is_student

def teacher_required(user):
    return user.is_active and user.is_teacher