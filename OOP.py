class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_score(self):
        if not self.grades:
            return 0
        average_score = []
        for grades_lecturer in self.grades.values():
            average_score.extend(grades_lecturer)
        return round(sum(average_score)/len(average_score),2)

    def __str__(self):
        finished_courses_list = ', '.join(self.finished_courses)
        courses_in_progress_list = ', '.join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_score()}\nКурсы в процессе изучения: {courses_in_progress_list}\nЗавершенные курсы: {finished_courses_list}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() < other.get_average_score()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() > other.get_average_score()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() == other.get_average_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}

    def get_average_score(self):
        if not self.grades:
            return 0
        average_score = []
        for grades_lecturer in self.grades.values():
            average_score.extend(grades_lecturer)
        return round(sum(average_score)/len(average_score),2)

    def __str__(self) ->str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_score()}\n"
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() < other.get_average_score()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() > other.get_average_score()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.get_average_score() == other.get_average_score()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) ->str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

Student1=Student('Ivan','Smirnov','your_gender')
Student2=Student('Mihail','Sidorov','your_gender')

Student1.courses_in_progress += ['Python']
Student1.courses_in_progress += ['Git']
Student1.finished_courses += ['Введение в программирование']

Student2.courses_in_progress += ['Python']
Student2.courses_in_progress += ['Git']
Student2.finished_courses += ['Введение в программирование']

Reviewer1 = Reviewer('Petrova','Mariya')
Reviewer2 = Reviewer('Belov', 'Andrey')

Reviewer1.courses_attached += ['Python']
Reviewer1.courses_attached += ['Git']

Reviewer1.rate_hw(Student1,'Python',10)
Reviewer1.rate_hw(Student1,'Python',9)
Reviewer1.rate_hw(Student1,'Python',7)

Reviewer1.rate_hw(Student1,'Git',10)
Reviewer1.rate_hw(Student1,'Git',10)
Reviewer1.rate_hw(Student1,'Git',8)

Reviewer2.courses_attached += ['Python']
Reviewer2.courses_attached += ['Git']

Reviewer2.rate_hw(Student2,'Python',9)
Reviewer2.rate_hw(Student2,'Python',9)
Reviewer2.rate_hw(Student2,'Python',7)

Reviewer2.rate_hw(Student2,'Git',10)
Reviewer2.rate_hw(Student2,'Git',9)
Reviewer2.rate_hw(Student2,'Git',8)

Lecturer1=Lecturer('Alexandr','Ivanov')
Lecturer2=Lecturer('Petr','Voronin')

Lecturer1.courses_attached += ['Python']
Lecturer1.courses_attached += ['Git']

Student1.rate_lect(Lecturer1,'Python',10)
Student1.rate_lect(Lecturer1,'Python',9)
Student1.rate_lect(Lecturer1,'Python',6)

Student1.rate_lect(Lecturer1,'Git',10)
Student1.rate_lect(Lecturer1,'Git',9)
Student1.rate_lect(Lecturer1,'Git',10)

Lecturer2.courses_attached += ['Python']
Lecturer2.courses_attached += ['Git']

Student2.rate_lect(Lecturer2,'Python',8)
Student2.rate_lect(Lecturer2,'Python',9)
Student2.rate_lect(Lecturer2,'Python',6)

Student2.rate_lect(Lecturer2,'Git',7)
Student2.rate_lect(Lecturer2,'Git',9)
Student2.rate_lect(Lecturer2,'Git',6)

print(Student1)
print(Student2)
print(Lecturer1)
print(Lecturer2)
print(Reviewer1)
print(Reviewer2)
print(f'Результат сравнения студентов по средним оценкам за домашние задания: '
      f'{Student1.name} {Student1.surname} {"<"if Student1<Student2 else (">" if Student1>Student2 else "=")} {Student2.name} {Student2.surname}')
print()
print(f'Результат сравнения лекторов по средним оценкам за лекции: '
      f'{Lecturer1.name} {Lecturer1.surname} {"<"if Lecturer1<Lecturer2 else (">" if Lecturer1>Lecturer2 else "=")} {Lecturer2.name} {Lecturer2.surname}')

list_student = [Student1, Student2]
list_lecturer = [Lecturer1, Lecturer2]
course_name='Python'
def average_grade_course(list_student, course_name):
    grades_list = []
    for student in list_student:
        grades_list.extend(student.grades.get(course_name, []))
    return round(sum(grades_list) / len(grades_list), 2)

def lecturer_grade_course(list_lecturer, course_name):
    return average_grade_course(list_lecturer, course_name)

print()
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {average_grade_course(list_student, 'Python')}")
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {average_grade_course(list_student, 'Git')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_grade_course(list_lecturer, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {lecturer_grade_course(list_lecturer, 'Git')}")
