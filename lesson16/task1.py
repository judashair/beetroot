class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_inf(self):
        return f"Good morning! My name is {self.first_name} {self.last_name} and I`m {self.age} years old!"


class Student(Person):
    def __init__(self, first_name, last_name, age, course, course_name):
        super().__init__(first_name, last_name, age)
        self.course_name = course_name
        self.course = course

    def show_student_info(self):
        return f"I`m learning at {self.course} course on {self.course_name}"


class Teacher(Person):

    def __init__(self, first_name, last_name, age, subject, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.subject = subject

    def show_teacher_info(self):
        return f"I`m teaching {self.subject} and has salary {self.salary} per month"


person = Person("Anna", "Samsonenko", 25)
person.show_inf()
student = Student("Oksana", "Samsonenko", 27, '5', "IB")
teacher = Teacher("Mike", "Bond", 48, "History", 1000)
print(person.show_inf())
print(student.show_inf())
print(student.show_student_info())
print(teacher.show_inf())
print(teacher.show_teacher_info())
