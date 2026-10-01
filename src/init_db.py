'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import Course

courses = [
    ('CS', '1050', 'Computer Science 1', 4),
    ('CS', '2050', 'Computer Science 2', 4),
    ('CS', '3250', 'Software Dev Methods & Tools', 3),
    ('MTH', '1110', 'College Algebra', 4),
    ('ENG', '1010', 'Composition', 3),
]

with app.app_context():
    for prefix, number, name, credits in courses:
        course = Course.query.get((prefix, number))
        if not course:
            course = Course(prefix=prefix, number=number, name=name, credits=credits)
            db.session.add(course)
    db.session.commit()
    print(f'Loaded {len(courses)} courses.')
