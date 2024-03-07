from sqlalchemy import func, desc, and_
from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result


def select_03():
    """
    SELECT
        gr.name AS group_name,
        AVG(g.grade) AS average_grade
    FROM groups gr
    JOIN students s ON gr.id = s.group_id
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 1
    GROUP BY gr.name;
    """
    result = session.query(Group.name.label('group_name'), func.avg(Grade.grade).label('average_grade')) \
        .select_from(Group).join(Student).join(Grade).filter(Grade.subjects_id == 1).group_by(Group.name).all()
    return result


def select_04():
    """
    SELECT
        AVG(grade) AS overall_average_grade
    FROM grades;
    """
    result = session.query(func.avg(Grade.grade).label('overall_average_grade')) \
        .select_from(Grade).all()
    return result


def select_05():
    """
    SELECT sub.name
    FROM subjects sub
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE t.fullname = 'Darryl Allen'; --замінити значення в залежності від таблиці
    """
    result = session.query(Subject.name) \
        .select_from(Subject).join(Teacher).filter(Teacher.fullname == 'Darryl Allen').all()
    return result


def select_06():
    """
    SELECT s.fullname
    FROM students s
    JOIN groups g ON s.group_id = g.id
    WHERE g.name = 'Group B'; --замінити значення в залежності від таблиці
    """
    result = session.query(Student.fullname) \
        .select_from(Student).join(Group).filter(Group.name == 'guy').all()
    return result


def select_07():
    """
    SELECT
        s.fullname,
        g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN groups gr ON s.group_id = gr.id
    WHERE gr.name = 'Group A' AND g.subject_id = 1; --замінити значення в залежності від таблиці
    """
    result = session.query(Student.fullname, Grade.grade) \
        .select_from(Student).join(Grade).join(Group).filter(and_(Group.name == 'American', Grade.subjects_id == 1)).all()
    return result


def select_08():
    """
    SELECT
        t.fullname,
        AVG(g.grade) AS average_grade
    FROM teachers t
    JOIN subjects sub ON t.id = sub.teacher_id
    JOIN grades g ON sub.id = g.subject_id
    WHERE t.fullname = 'Paul Klein' --замінити значення в залежності від таблиці
    GROUP BY t.fullname;
    """
    result = session.query(Teacher.fullname, func.avg(Grade.grade).label('average_grade')) \
        .select_from(Teacher).join(Subject).join(Grade).filter(Teacher.fullname == 'Laura Bridges') \
        .group_by(Teacher.fullname).all()
    return result


def select_09():
    """
    SELECT DISTINCT sub.name
    FROM subjects sub
    JOIN grades g ON sub.id = g.subject_id
    JOIN students s ON g.student_id = s.id
    WHERE s.fullname = 'John Cox'; --замінити значення в залежності від таблиці
    """
    result = session.query(Subject.name).distinct() \
        .join(Grade).join(Student).filter(Student.fullname == 'John Cox').all()
    return result


def select_10():
    """
    SELECT DISTINCT sub.name
    FROM subjects sub
    JOIN grades g ON sub.id = g.subject_id
    JOIN students s ON g.student_id = s.id
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE s.fullname = 'Molly Leon' AND t.fullname = 'Darryl Allen'; --замінити значення в залежності від таблиці
    """
    result = session.query(Subject.name).distinct().join(Grade).join(Student) \
        .join(Teacher).filter(Student.fullname == 'Molly Leon', Teacher.fullname == 'Darryl Allen').all()
    return result


if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03())
    print(select_04())
    print(select_05())
    print(select_06())
    print(select_07())
    print(select_08())
    print(select_09())
    print(select_10())