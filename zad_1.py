class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50


# Test
student_1 = Student('majkel dżekson', 60)
student_2 = Student('tina turner', 30)

print(f'Student_1: {student_1.is_passed()}')
print(f'Student_2: {student_2.is_passed()}')
