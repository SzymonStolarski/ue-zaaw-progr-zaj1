from .employee import Employee
from .student import Student


class Order:
    """
    Class storing the info about particular order
    """
    def __init__(self, employee: Employee, student: Student, books: list,
                 order_date: str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f'Order issued by: {self.employee}, \
                 order placed by: {self.student}, \
                 ordered books: {self.books}, \
                 order date: {self.order_date}'
