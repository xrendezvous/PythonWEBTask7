from faker import Faker
import random
from conf.db import session
from conf.models import Student, Group, Teacher, Subject, Grade

faker = Faker()

groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)
session.commit()

teachers = []
for _ in range(3):
    teacher = Teacher(fullname=faker.name())
    teachers.append(teacher)
    session.add(teacher)
session.commit()

subjects = ['Drama', 'Business', 'Literature', 'Biology', 'History']
for subject_name in subjects:
    subject = Subject(name=subject_name, teacher_id=random.choice(teachers).id)
    session.add(subject)
session.commit()

for _ in range(50):
    group_id = random.choice(session.query(Group.id).all())[0]
    student = Student(fullname=faker.name(), group_id=group_id)
    session.add(student)
    session.commit()
    for _ in range(random.randint(5, 20)):
        subject_id = random.choice(session.query(Subject.id).all())[0]
        grade = Grade(grade=random.randint(1, 5), grade_date=faker.date_between(start_date='-1y', end_date='today'), student_id=student.id, subjects_id=subject_id)
        session.add(grade)
    session.commit()
