class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.average_rating = float()
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашнее задание: {self.average_rating} \n' \
               f'Курсы в процессе изучение: {courses_in_progress_string} \n' \
               f'Завершенный курсы: {finished_courses_string} '

    def __eq__(self, grade):
        if student1 == student2:
            print("Средняя оценка одинаковая")
        else:
            print("Оценки не равны")
        return self.grades == grade.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating}"

    def __eq__(self, grade):
        if lecturer1 == lecturer2:
            print("Средняя оценка одинаковая")
        else:
            print("Оценки не равны")
        return self.grades == grade.grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


# Оцениваем студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_rev = Reviewer('Some', 'Buddy')
cool_rev.courses_attached += ['Python']

cool_rev.rate_hw(best_student, 'Python', 10)
cool_rev.rate_hw(best_student, 'Python', 10)
cool_rev.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

# Оцениваем лекторов
best_student = Student("Shi", "Chi", "women")
best_student.courses_in_progress += ["Git"]

cool_lector = Lecturer("Dima", "May")
cool_lector.courses_attached += ["Git"]

best_student.rate_hw(cool_lector, "Git", 10)
best_student.rate_hw(cool_lector, "Git", 8)
best_student.rate_hw(cool_lector, "Git", 9)

print(cool_lector.grades)
print()

# Перегрузка __str__
reviewer1 = Reviewer("Chan", 'Shi')
print(reviewer1)
print()

lecturer1 = Lecturer("Tlen", "Alen")
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer("Til", "Shvaiger")
lecturer2.courses_attached += ["Python"]

print(lecturer1)
print()

print(lecturer2)
print()

student1 = Student("Nikolay", "Pupkin", "men")
student2 = Student("Alik", "Bolduin", "men")
student1.courses_in_progress += ["Python"]
student1.finished_courses += ["Введение в программирование"]
student2.courses_in_progress += ["Python"]
student2.finished_courses += ["Введение в программирование"]

print(student1)
print()

print(student2)
print()

# Сравнение по студентам
print(f'Результат сравнения студентов: '
      f'{student1.name} {student1.surname} = {student2.name} {student2.surname}')
print()

# Сравнение по лекторам
print(f'Результат сравнения лекторов: '
      f'{lecturer1.name} {lecturer1.surname} = {lecturer2.name} {lecturer2.surname}')
print()

# Создаем список студентов
stud_list = [student1, student2]

# Создаем список лекторов
lecturer_list = [lecturer1, lecturer2]


def student_rating(stud_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in stud_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка студентов по курсу {'Python'}: {student_rating(stud_list, 'Python')}")
print()

print(f"Средняя оценка лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
