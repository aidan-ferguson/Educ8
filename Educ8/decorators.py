def is_student(user):
    return user.is_active and user.is_student

def is_teacher(user):
    return user.is_active and user.is_teacher