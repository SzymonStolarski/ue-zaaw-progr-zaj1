from library_system import *


library_1 = Library('koziegłowy', 'czarnowiejska', '23-123', '16-23', '123456')
library_2 = Library('zielone głowy', 'krótka', '22-111', '13-23', '123456')

book_1 = Book(library_1, 'pan tadeusz', 'adam', 'mickiewicz', 1000)
book_2 = Book(library_1, 'pan mariusz', 'adam', 'plackiewicz', 300)
book_3 = Book(library_1, 'pan eugeniusz', 'michal', 'mickiewicz', 1000)
book_4 = Book(library_2, 'pan zdzisiek', 'donald', 'kaczynski', 1000)
book_5 = Book(library_2, 'hokus pokus', 'majkel', 'dzekson', 1000)

employee_1 = Employee('majkel', 'dzekson', '03.02.1990', '03.05.1950',
                      'zebrzydowice', 'gornoslaska', '22-333')
employee_2 = Employee('olgierd', 'czolgista', '03.06.1991', '03.05.1940',
                      'zebrzydowice', 'dolnoslaska', '22-333')
employee_3 = Employee('maryna', 'razdwatrzy', '03.02.1990', '03.05.1920',
                      'zebrzydowice', 'krotka', '22-333')

student_1 = Student('majkel', 'dzekson', 11111111111)
student_2 = Student('obama', 'binladen', 11111454511)
student_3 = Student('tina', 'turner', 22211111111)

order_1 = Order(employee_1, student_2, [book_1, book_3], '01.01.2020')
order_2 = Order(employee_2, student_1, [book_2, book_5], '01.02.2020')

# Show both the orders
print(order_1)
print(order_2)
