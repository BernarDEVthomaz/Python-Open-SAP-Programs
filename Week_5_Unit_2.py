def get_student_data():
    name = input("Please, enter your name:")
    first_name = input("Please, enter your first name:")
    student_id = input("Please, enter your ID:")
    data = (name, first_name, student_id)
    return data

student_data = get_student_data()
print(student_data)
