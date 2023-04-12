from typing import Dict


class Subject:
    def __int__(self, subject_name: str, teacher_name: str):
        self.subject_name = subject_name
        self.teacher_name = teacher_name


class Test:
    def __int__(self, test_date: str, test_subject: Subject):
        self.test_date = test_date
        self.test_subject = test_subject


class ClassRoom:
    def __int__(self):
        self.members = []
        self.room: int = -1

    def add_to_classroom(self, student: 'Student'):
        self.members.append(student)

    def set_room(self, room_number: int):
        self.room = room_number


class Student:
    def __int__(self, id_number: str, name: str):
        self.id_number = id_number
        self.name = name
        self.subjects_dict = Dict[str, Subject] = {}
        self.classroom = None
        self.grades_dict = Dict[Test, list] = {}

    def register_to_class(self, classroom: ClassRoom):
        classroom.add_to_classroom(self)
        self.classroom = classroom

    def add_subject(self, subject: Subject):
        self.subjects_dict[subject.subject_name] = subject

    def remove_subject(self, subject: Subject):
        if subject.subject_name in self.subjects_dict:
            self.subjects_dict.pop(subject.subject_name)

    def add_grade(self, test: Test, grade: int):
        try:
            self.grades_dict[test.test_subject.subject_name].append(grade)
        except KeyError:
            self.grades_dict[test.test_subject.subject_name] = []
            self.grades_dict[test.test_subject.subject_name].append(grade)

    def average_grade(self) -> Dict[str, int]:
        average_dict = dict()
        for grade_name in self.grades_dict:
            average_dict[grade_name] = sum(self.grades_dict[grade_name]) / len(self.grades_dict[grade_name])
        return average_dict

print("---------------------------------------")


eitam = Student("215988353", "Eitam")
English = Subject("English", "Revital")
Math = Subject("Math", "Yohi")
Computers = Subject("Computers", "Talya")

eitam.add_subject(English)
eitam.add_subject(Math)
eitam.add_subject(Computers)

Math_test1 = Test(Math, "1/11/22")
Math_test2 = Test(Math, "15/02/23")
Math_test3 = Test(Math, "18/03/23")
English_test_1 = Test(English, "25/12/22")
Computers_test_1 = Test(Computers, "18/01/22")

eitam.add_grade(Math_test1, 100)
eitam.add_grade(Math_test2, 92)
eitam.add_grade(Math_test3, 87)
eitam.add_grade(English_test_1, 87)
eitam.add_grade(Computers_test_1, 98)

print(eitam.subjects_dict)
print(eitam.grades_dict)
print(eitam.average_grade())





