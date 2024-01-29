import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents, Person

# Define fixture for a sample classroom with a teacher and 5 students
@pytest.fixture
def sample_classroom():
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student {i+1}") for i in range(5)]
    course_title = "Transfiguration"
    return Classroom(teacher, students, course_title)

# Test add_student function
def test_add_student(sample_classroom):
    # Add a student to the classroom
    new_student = Student("Harry Potter")
    sample_classroom.add_student(new_student)
    assert len(sample_classroom.students) == 6

    # Adding more than 10 students should raise TooManyStudents exception
    with pytest.raises(TooManyStudents):
        for i in range(6, 15):
            sample_classroom.add_student(Student(f"Extra Student {i}"))

# Test remove_student function
def test_remove_student(sample_classroom):
    # Remove an existing student from the classroom
    sample_classroom.remove_student("Student 3")
    assert len(sample_classroom.students) == 4

    # Try removing a non-existing student, should not raise an exception
    sample_classroom.remove_student("Nonexistent Student")

# Test change_teacher function
def test_change_teacher(sample_classroom):
    # Change the teacher of the classroom
    new_teacher = Teacher("Professor Snape")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher.name == "Professor Snape"

# Test the Person class
def test_person_class():
    # Create a person and check if the name is set correctly
    person = Person("Albus Dumbledore")
    assert person.name == "Albus Dumbledore"

# Test the Teacher class
def test_teacher_class():
    # Create a teacher and check if the name is set correctly
    teacher = Teacher("Professor Flitwick")
    assert teacher.name == "Professor Flitwick"

# Test the Student class
def test_student_class():
    # Create a student and check if the name is set correctly
    student = Student("Ron Weasley")
    assert student.name == "Ron Weasley"
